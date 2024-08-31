import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import VadGraph from './components/VadGraph'; // Import the VadGraph component
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  const [graphUrl, setGraphUrl] = useState('');

  return (
    <div className="flex flex-col bg-slate-100 min-h-screen">
      <Header />
      <div className="flex flex-grow flex-col">
        <main className="flex-1 overflow-auto p-4">
          <FileUpload onGraphUrl={setGraphUrl} />
          {/* Render the VadGraph component */}
          <div className="mt-8 w-full flex justify-center items-center">
            {graphUrl ? (
              <VadGraph imageUrl={graphUrl} />
            ) : (
              <p className="text-lg text-gray-600">Audio waveform will appear here.</p>
            )}
          </div>
        </main>
      </div>
      <Footer />
    </div>
  );
}

export default App;
