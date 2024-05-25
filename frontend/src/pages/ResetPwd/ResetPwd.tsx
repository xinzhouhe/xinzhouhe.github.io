import React, { useEffect, useState } from 'react';
import { Helmet } from 'react-helmet';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';
import Header from '../../components/Utils/Header';
import ResetPwdLink from '../../components/Auth/ResetPwdLink';
import ResetPwdForm from '../../components/Auth/ResetPwdForm';
import '../Login/Login.css';

const ResetPwd: React.FC = () => {
  const [isValidToken, setIsValidToken] = useState<boolean | null>(null);
  const location = useLocation();
  const navigate = useNavigate();

  useEffect(() => {
    const query = new URLSearchParams(location.search);
    const token = query.get('token');

    if (location.pathname === '/reset-password/change-password' && token) {
      axios.get(`http://localhost:5000/auth/validate_reset_token/${token}`)
        .then(response => {
          if (response.status === 200) {
            setIsValidToken(true);
          } else {
            navigate('/');
          }
        })
        .catch(() => {
          navigate('/');
        });
    } else if (location.pathname !== '/reset-password/send-link') {
      navigate('/');
    }
  }, [location, navigate]);

  const renderComponent = () => {
    if (location.pathname === '/reset-password/send-link') {
      return <ResetPwdLink />;
    } else if (location.pathname === '/reset-password/change-password') {
      if (isValidToken === null) {
        return <div>Loading...</div>;
      } else if (isValidToken) {
        return <ResetPwdForm />;
      } else {
        return null;
      }
    } else {
      return null;
    }
  };

  return (
    <div className="login-page">
      <Helmet>
        <title>TransferMax - Reset your password</title>
      </Helmet>
      <header className="bg-white shadow-md">
        <div className="container mx-auto flex justify-between items-center py-4 px-6">
          <Header />
        </div>
      </header>
      {renderComponent()}
    </div>
  );
};

export default ResetPwd;
