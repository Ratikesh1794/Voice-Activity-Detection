import React, { useState } from 'react';
import { SiAudiomack } from "react-icons/si";

const FileUpload = ({ onResults }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (file.type === 'audio/mpeg' || file.type === 'audio/mp3') {
        setSelectedFile(file);
        setError(null);
      } else {
        setError('Please upload an MP3 file.');
        setSelectedFile(null);
      }
    }
  };

  const handleFileUpload = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await fetch('http://127.0.0.1:5000/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const data = await response.json();
          if (data.timestamps) {
            onResults(data.timestamps);
          } else {
            alert('No voice activity detected.');
          }
        } else {
          const errorData = await response.json();
          alert(`Error: ${errorData.message || 'Failed to upload file.'}`);
        }
      } catch (error) {
        console.error('Error uploading file:', error);
        alert('An error occurred during file upload.');
      }
    } else {
      alert('No file selected.');
    }
  };

  return (
    <div className="flex p-1">
      <div className="w-1/2 bg-blue-700 flex items-center justify-center rounded-s-full">
        <h1>
          <SiAudiomack className="text-9xl text-blue-700 bg-white rounded-r-full" />
        </h1>
      </div>

      <div className="w-1/2 flex items-center justify-center bg-slate-200 shadow-lg">
        <div className="max-w-md w-full">
          <h2 className="text-4xl font-semibold text-gray-800 mb-20">Upload MP3 File</h2>
          <div className="mb-4">
            <input
              type="file"
              accept=".mp3"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 focus:outline-none"
            />
            {error && <p className="text-red-500 text-sm mt-2">{error}</p>}
          </div>
          <button
            onClick={handleFileUpload}
            className="w-full py-2 px-4 bg-blue-600 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75"
          >
            Upload MP3
          </button>
          {selectedFile && (
            <p className="mt-4 text-gray-700 text-sm">
              Selected file: <span className="font-medium">{selectedFile.name}</span>
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default FileUpload;
