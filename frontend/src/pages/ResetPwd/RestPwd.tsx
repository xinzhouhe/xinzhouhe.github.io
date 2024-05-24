import React from 'react';
import { Helmet } from 'react-helmet';
import Header from '../../components/Utils/Header';
import ResetPwdFrom from '../../components/Auth/ResetPwdForm';
import '../Login/Login.css';

const ResetPwd: React.FC = () => {
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
        <ResetPwdFrom />
      </div>
  );
};

export default ResetPwd;
