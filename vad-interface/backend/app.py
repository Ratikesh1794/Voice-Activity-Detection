from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from io import BytesIO
import json

app = Flask(__name__)
CORS(app)  # Enable CORS
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3'}

def perform_vad(audio_segment):
    # Simple VAD placeholder; this needs to be replaced with an actual VAD algorithm.
    # Here we just segment the audio into fixed intervals for demonstration purposes.
    duration_ms = len(audio_segment)
    interval = 5000  # 5 seconds
    segments = []
    for start in range(0, duration_ms, interval):
        end = min(start + interval, duration_ms)
        segments.append({
            'start_time': start / 1000.0,
            'end_time': end / 1000.0
        })
    return segments

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)

            # Load the audio file
            audio = AudioSegment.from_mp3(filename)

            # Perform Voice Activity Detection
            vad_results = perform_vad(audio)

            # Generate and return audio waveform
            return generate_waveform_image(filename, vad_results)

        except Exception as e:
            return jsonify({'status': 'error', 'message': f'Failed to process file: {str(e)}'}), 500

    return jsonify({'status': 'error', 'message': 'Invalid file type. Only MP3 files are allowed.'}), 400

def generate_waveform_image(mp3_path, vad_results):
    # Load the audio file
    audio = AudioSegment.from_mp3(mp3_path)
    sample_rate = audio.frame_rate
    audio_samples = np.array(audio.get_array_of_samples())
    duration_seconds = len(audio_samples) / sample_rate
    time = np.linspace(0, duration_seconds, len(audio_samples))

    # Plot waveform
    plt.figure(figsize=(12, 6))
    plt.plot(time, audio_samples, color='grey', label='Waveform')

    # Adding labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform with Voice Activity')
    plt.legend(loc='upper right')

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Return the image as a response
    return send_file(img, mimetype='image/png', as_attachment=True, download_name='waveform.png')

if __name__ == '__main__':
    app.run(debug=True)
