import numpy as np
import wave
import webrtcvad

def read_wave(path):
    try:
        with wave.open(path, 'rb') as wf:
            sample_rate = wf.getframerate()
            num_channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            num_frames = wf.getnframes()
            audio_data = wf.readframes(num_frames)
        
        if num_channels != 1:
            raise ValueError("Only mono audio files are supported.")
        if sample_width != 2:
            raise ValueError("Only 16-bit audio is supported.")
        
        return np.frombuffer(audio_data, dtype=np.int16), sample_rate
    except Exception as e:
        print(f"Error reading wave file: {str(e)}")
        raise

def frame_generator(frame_duration_ms, audio, sample_rate):
    try:
        n = int(sample_rate * frame_duration_ms / 1000 * 2)
        offset = 0
        while offset + n <= len(audio):
            yield audio[offset:offset + n]
            offset += n
    except Exception as e:
        print(f"Error generating frames: {str(e)}")
        raise

def vad_collector(sample_rate, frame_duration_ms, padding_duration_ms, vad, frames):
    try:
        num_padding_frames = int(padding_duration_ms / frame_duration_ms)
        ring_buffer = []
        triggered = False

        voiced_frames = []
        timestamps = []
        start_time = 0

        frame_index = 0
        for frame in frames:
            is_speech = vad.is_speech(frame, sample_rate)
            frame_time = frame_index * frame_duration_ms / 1000.0

            if not triggered:
                ring_buffer.append((frame, frame_time))
                num_voiced = sum(1 for f, _ in ring_buffer if vad.is_speech(f, sample_rate))
                if num_voiced > 0.9 * len(ring_buffer):
                    triggered = True
                    start_time = ring_buffer[0][1]
                    ring_buffer = []
            else:
                voiced_frames.append(frame)
                if not is_speech:
                    ring_buffer.append((frame, frame_time))
                    if len(ring_buffer) > num_padding_frames:
                        triggered = False
                        end_time = ring_buffer[0][1]
                        timestamps.append((start_time, end_time))
                        ring_buffer = []

            frame_index += 1

        if triggered:
            timestamps.append((start_time, frame_time))

        return timestamps
    except Exception as e:
        print(f"Error in VAD collector: {str(e)}")
        raise

def process_audio(filepath):
    try:
        audio, sample_rate = read_wave(filepath)
        vad = webrtcvad.Vad()
        frames = list(frame_generator(30, audio, sample_rate))
        timestamps = vad_collector(sample_rate, 30, 300, vad, frames)
        return timestamps
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        raise
