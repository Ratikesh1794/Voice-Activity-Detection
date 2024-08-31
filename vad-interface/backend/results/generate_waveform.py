import json
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

def plot_waveform(mp3_path, json_path, output_image_path):
    # Load the audio file
    audio = AudioSegment.from_mp3(mp3_path)
    sample_rate = audio.frame_rate
    audio_samples = np.array(audio.get_array_of_samples())
    duration_seconds = len(audio_samples) / sample_rate
    time = np.linspace(0, duration_seconds, len(audio_samples))
    
    # Load VAD results from JSON
    with open(json_path, 'r') as f:
        vad_results = json.load(f)
    
    # Plot waveform
    plt.figure(figsize=(12, 6))
    plt.plot(time, audio_samples, color='grey', label='Waveform')
    
    # Plot voice activity segments
    for segment in vad_results:
        plt.axvspan(segment['start_time'], segment['end_time'], color='red', alpha=0.5, label='Voice Activity')

    # Adding labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform with Voice Activity')
    plt.legend(loc='upper right')

    # Save the plot as an image file
    plt.savefig(output_image_path)
    plt.show()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate waveform from MP3 and VAD results")
    parser.add_argument("mp3_path", help="Path to the input MP3 file")
    parser.add_argument("json_path", help="Path to the VAD results JSON file")
    parser.add_argument("output_image_path", help="Path to save the waveform image")
    args = parser.parse_args()
    
    plot_waveform(args.mp3_path, args.json_path, args.output_image_path)
