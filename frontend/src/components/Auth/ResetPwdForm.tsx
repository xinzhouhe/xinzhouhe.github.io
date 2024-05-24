import React, { useState } from 'react';

const ResetPwdForm: React.FC = () => {
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState('');

  const validateEmail = (email: string) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    if (email === '') {
      setEmailError('Email cannot be empty');
    } else if (!validateEmail(email)) {
      setEmailError('Email is not valid');
    } else {
      setEmailError('');
      // Proceed with sending reset link
      console.log('Reset link sent to', email);
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
          <button className="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit">Send Reset Link</button>
        </form>
        <p className="text-center text-gray-600 mt-6 hover:underline">
          <a href="/login">Return to Log in</a>
        </p>
      </div>
    </div>
  );
};

export default ResetPwdForm;
