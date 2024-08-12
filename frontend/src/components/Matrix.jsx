// src/Matrix.js
import React, { useEffect, useState } from 'react';
import './Matrix.css'; // Make sure this file exists

const Matrix = () => {
  const [frequencyMap, setFrequencyMap] = useState({});
  const [selectedBox, setSelectedBox] = useState([]);

  useEffect(() => {
    // Fetch the frequency map from your Flask backend
    fetch('http://localhost:8080/frequency-map')
      .then(response => response.json())
      .then(data => setFrequencyMap(data))
      .catch(error => console.error('Error fetching frequency map:', error));
  }, []);

  // Determine the matrix size based on frequencyMap
  const size = Math.sqrt(Object.keys(frequencyMap).length); // Assuming a square matrix

  const handleClick = (key) => {
    // Prevent re-clicking on already revealed boxes
    if (selectedBox.includes(key)) return;

    setSelectedBox([...selectedBox, key]);
  };
  const getSingleIndex = (row, col) => row * size + col;
  return (
    <div className="matrix-container">
      {Array.from({ length: size }).map((_, rowIndex) => (
        <div key={rowIndex} className="matrix-row">
          {Array.from({ length: size }).map((_, colIndex) => {
            const key = getSingleIndex(rowIndex, colIndex); // Use row-col format for keys
            const value = frequencyMap[key] || 'Unknown';
            const isRevealed = selectedBox.includes(key);

            // Determine the face based on the value
            const face = value === 'The object is a Mine' ? '😊' : value === 'The object is a Rock' ? '😔' : '?';

            return (
              <div
                key={colIndex}
                className={`matrix-box ${isRevealed ? value.toLowerCase() : 'hidden'}`}
                onClick={() => handleClick(key)}
                style={{ cursor: isRevealed ? 'not-allowed' : 'pointer' }} // Disable click on revealed boxes
              >
                <div className={`face ${isRevealed ? 'visible' : 'hidden'}`}>
                  {face}
                </div>
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
};

export default Matrix;
