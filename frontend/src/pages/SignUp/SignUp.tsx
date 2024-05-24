import React from 'react';
import { Helmet } from 'react-helmet';
import Header from '../../components/Utils/Header';
import SignupForm from '../../components/Auth/SignupForm';
import './SignUp.css';

const Signup: React.FC = () => {
  return (
      <div className="signup-page">
        <Helmet>
          <title>TransferMax - Sign Up</title>
        </Helmet>
        <header className="bg-white shadow-md">
          <div className="container mx-auto flex justify-between items-center py-4 px-6">
            <Header />
          </div>
        </header>
        <SignupForm />
      </div>
  );
};

export default Signup;