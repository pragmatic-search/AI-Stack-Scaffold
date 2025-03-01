import React, { useEffect, useState } from 'react';

function App() {
  const [backendData, setBackendData] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000')
      .then(res => res.json())
      .then(data => setBackendData(data));
  }, []);

  return (
    <div>
      <h1>Prodigal AI Full Stack</h1>
      <p>Backend response: {backendData.message || "Loading..."}</p>
    </div>
  );
}

export default App;