import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import VadResults from './components/VadResults';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  const [timestamps, setTimestamps] = useState([]);

  return (
    <div className="flex flex-col bg-slate-100 min-h-screen">
      <Header />
      <div className="flex flex-grow flex-col">
        <main className="flex-1 overflow-auto p-4">
          <FileUpload onResults={setTimestamps} />
          {timestamps.length > 0 && <VadResults timestamps={timestamps} />}
        </main>
      </div>
      <Footer />
    </div>
  );
}

export default App;
