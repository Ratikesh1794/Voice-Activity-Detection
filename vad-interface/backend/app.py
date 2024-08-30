from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS to handle CORS issues
import os
import json
from vad import perform_vad  # Ensure your VAD function is correctly imported

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
RESULTS_FOLDER = 'results'
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and file.filename.endswith('.mp3'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_file.mp3')
        file.save(filepath)

        # Perform VAD
        try:
            timestamps = perform_vad(filepath)  # Ensure this function is implemented correctly

            # Save timestamps to a JSON file
            results_filepath = os.path.join(RESULTS_FOLDER, 'timestamps.json')
            with open(results_filepath, 'w') as f:
                json.dump(timestamps, f)

            return jsonify({'timestamps': timestamps})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
