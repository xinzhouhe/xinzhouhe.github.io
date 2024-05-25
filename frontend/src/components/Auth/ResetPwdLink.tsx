import React, { useState } from 'react';
import axios from 'axios';

const ResetPwdLink: React.FC = () => {
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState('');
  const [resetError, setResetError] = useState('');
  const [resetSuccess, setResetSuccess] = useState('');

  const validateEmail = (email: string) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    if (email === '') {
      setEmailError('Email cannot be empty');
      return;
    } else if (!validateEmail(email)) {
      setEmailError('Email is not valid');
      return;
    } else {
      setEmailError('');
    }

    try {
      const response = await axios.post('http://localhost:5000/auth/send_reset_link', { email });

      if (response.status === 200) {
        setResetSuccess('Reset link sent successfully');
        setResetError('');
      } else {
        setResetError('Failed to send reset link');
        setResetSuccess('');
      }
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        setResetError(error.response.data.message);
      } else {
        setResetError('An error occurred. Please try again.');
      }
      setResetSuccess('');
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="bg-white p-8 rounded shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold text-blue-600 mb-6 text-center">Reset Your Password</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="email">Email address</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            {emailError && <p className="text-red-500 text-sm mt-1">{emailError}</p>}
          </div>
          {resetError && <p className="text-red-500 text-sm mb-4">{resetError}</p>}
          {resetSuccess && <p className="text-green-500 text-sm mb-4">{resetSuccess}</p>}
          <button className="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit">Send Reset Link</button>
        </form>
        <p className="text-center text-gray-600 mt-6 hover:underline">
          <a href="/login">Return to Log in</a>
        </p>
      </div>
    </div>
  );
};

export default ResetPwdLink;
