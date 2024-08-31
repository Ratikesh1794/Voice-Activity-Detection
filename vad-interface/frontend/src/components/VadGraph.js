import React from 'react';

const VadGraph = ({ imageUrl }) => {
  return (
    <div className="w-full max-w-4xl mx-auto p-4 bg-white shadow-lg rounded-lg">
      <h2 className="text-2xl font-semibold text-gray-800 mb-4">Audio Graph</h2>
      <div className="flex justify-center">
        <img src={imageUrl} alt="Audio Graph" className="max-w-full h-auto rounded-lg" />
      </div>
    </div>
  );
};

export default VadGraph;
