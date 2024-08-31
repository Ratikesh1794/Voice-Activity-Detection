## VAD Interface Project

![image](https://github.com/user-attachments/assets/1c6f40bf-31e6-412d-8adc-de6831265226)


**Overview**

This project is a web-based application that allows users to upload MP3 audio files and perform Voice Activity Detection (VAD) on the uploaded audio. The application detects silent and non-silent segments within the audio file and displays the timestamps where voice activity occurs.

**Key Features**

* **File Upload Interface:** Users can upload MP3 files for processing.
* **Voice Activity Detection (VAD):** The backend processes the audio file to identify sections where voice activity occurs.
* **Results Display:** Timestamps of detected voice activity are displayed to the user.

**Technologies Used**

* Frontend: ReactJS, Tailwind CSS
* Backend: Flask (Python)
* Other: HTML, CSS, JavaScript

**Installation Guide**

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/vad-interface.git
cd vad-interface
```

2. **Backend Setup**

**a. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**b. Install Backend Dependencies**

```bash
cd backend
pip install flask
pip install flask-cors
pip install numpy
pip install matplotlib
pip install pydub
```

Also install ffmpeg based on OS
Link : https://ffmpeg.org/download.html#build-windows

**c. Run the Flask Server**

```bash
python app.py
```

3. **Frontend Setup**

**a. Navigate to the Frontend Directory**

```bash
cd frontend
```

**b. Install Node.js Dependencies**

```bash
npm install
```

**c. Start the React Application**

```bash
npm start
```

4. **Run the Application**

* Ensure the Flask server is running on http://127.0.0.1:5000.
* Ensure the React frontend is running on http://127.0.0.1:3000.

5. **Usage**

* Open your web browser and go to http://127.0.0.1:3000.
* Use the "Upload MP3" button to upload an MP3 file.
* After uploading, the application will process the file and display the timestamps where voice activity is detected.

**Project Structure**

```
vad-interface/
├── backend/
│   ├── app.py (Flask application)
│   ├── uploads/ (Folder to store uploaded MP3 files)
│   └── requirements.txt (Backend dependencies)
├── frontend/
│   ├── node_modules/ (Installed Node.js packages)
│   ├── public/ (Static files served by React)
│   ├── src/ (React application source code)
│   │   ├── components/ (Reusable React components)
│   │   │   ├── FileUpload.js (File upload component)
│   │   │   ├── Header.js (Header component)
│   │   │   ├── Footer.js (Footer component)
│   │   │   └── VadGraph.js (Component to display VAD results)
│   │   ├── App.js (Main React application component)
│   │   ├── index.js (Entry point for the React application)
│   ├── package.json (Frontend dependencies and scripts)
│   ├── package-lock.json (Lock file for installed dependencies)
│   └── tailwind.config.js (Tailwind CSS configuration)
├── README.md (This file)
└── .gitignore (Git ignore file)
```

**Contributing**

Feel free to submit issues, fork the repository, and create pull requests. Contributions are welcome!
