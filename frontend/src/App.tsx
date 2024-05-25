// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login/Login';
import Home from './pages/HomePage/HomePage';
import Signup from './pages/SignUp/SignUp';
import ResetPwd from './pages/ResetPwd/ResetPwd';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/reset-password/send-link" element={<ResetPwd />} />
        <Route path="/reset-password/change-password" element={<ResetPwd />} />
      </Routes>
    </Router>
  );
};

export default App;
