import React from 'react';
import Hello from './Hello';
import './App.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Hello name="World" />
      </header>
    </div>
  );
};

export default App;
