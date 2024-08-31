import React, { useState } from 'react';
import axios from 'axios';
import { SiAudiomack } from "react-icons/si";

const FileUpload = ({ onGraphUrl }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setError('');
    setSuccess('');
  };

  const handleFileUpload = async () => {
    if (!selectedFile) {
      setError('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob'  // Important for handling image responses
      });

      if (response.status === 200) {
        setSuccess('File uploaded successfully.');

        // Create a URL for the PNG image
        const imageUrl = URL.createObjectURL(new Blob([response.data], { type: 'image/png' }));
        onGraphUrl(imageUrl);

        setSelectedFile(null); // Clear the file input
      } else {
        setError(`Failed to upload file: ${response.data.message}`);
      }
    } catch (error) {
      setError(`An error occurred during the file upload: ${error.message}`);
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
        <div className="max-w-md w-full p-6">
          <h2 className="text-4xl font-semibold text-gray-800 mb-6">Upload MP3 File</h2>
          <div className="mb-4">
            <input
              type="file"
              accept=".mp3"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-600 mb-6 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 focus:outline-none"
            />
            {error && <p className="text-red-500 text-sm mt-2">{error}</p>}
            {success && <p className="text-green-500 text-sm mt-2">{success}</p>}
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
