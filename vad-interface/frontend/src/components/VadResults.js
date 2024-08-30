import React from 'react';

const VadResults = ({ timestamps }) => {
  if (timestamps.length === 0) {
    return <div className="p-4 text-gray-700">No voice activity detected.</div>;
  }

  return (
    <div className="p-4">
      <h2 className="text-2xl font-semibold text-gray-800 mb-4">VAD Results</h2>
      <ul className="list-disc pl-5">
        {timestamps.map((timestamp, index) => (
          <li key={index} className="mb-2">
            {`Start: ${timestamp.start.toFixed(2)} s, End: ${timestamp.end.toFixed(2)} s`}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VadResults;
