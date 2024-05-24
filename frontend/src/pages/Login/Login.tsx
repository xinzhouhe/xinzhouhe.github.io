// src/pages/Login.tsx
import React from 'react';
import { Helmet } from 'react-helmet';
import Header from '../../components/Utils/Header';
import LoginForm from '../../components/Auth/LoginForm';
import './Login.css';

const Login: React.FC = () => {
  return (
      <div className="login-page">
        <Helmet>
          <title>TransferMax - Log in</title>
        </Helmet>
        <header className="bg-white shadow-md">
          <div className="container mx-auto flex justify-between items-center py-4 px-6">
            <Header />
          </div>
        </header>
        <LoginForm />
      </div>
  );
};

export default Login;
