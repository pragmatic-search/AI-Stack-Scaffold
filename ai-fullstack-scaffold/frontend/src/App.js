import React, { useState } from 'react';
import Auth from './components/Auth';
import Chatbot from './components/Chatbot';
import './styles.css';

function App() {
  const [user, setUser] = useState(null);

  return (
    <div className="app">
      <h1>Prodigal AI</h1>
      {!user ? <Auth onLogin={setUser} /> : <Chatbot />}
    </div>
  );
}

export default App;