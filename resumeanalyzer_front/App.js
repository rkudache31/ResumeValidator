// App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [logUrl, setLogUrl] = useState('');
  const [jdUrl, setJdUrl] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch(`http://172.210.90.153/validate/analyze?log_url=${encodeURIComponent(logUrl)}&jd_url=${encodeURIComponent(jdUrl)}`);
    const data = await response.text();
    setResult(data);
  };

  return (
    <div className="App">
      <h1>Resume Analyzer</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Log URL:
          <input type="text" value={logUrl} onChange={(e) => setLogUrl(e.target.value)} />
        </label>
        <br />
        <label>
          JD URL:
          <input type="text" value={jdUrl} onChange={(e) => setJdUrl(e.target.value)} />
        </label>
        <br />
        <button type="submit">Analyze</button>
      </form>
      {result && <div dangerouslySetInnerHTML={{ __html: result }}></div>}
    </div>
  );
}

export default App;

