import React, { useState } from 'react';

const LoginForm: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const validateEmail = (email: string) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    let valid = true;

    if (email === '') {
      setEmailError('Email cannot be empty');
      valid = false;
    } else if (!validateEmail(email)) {
      setEmailError('Email is not valid');
      valid = false;
    } else {
      setEmailError('');
    }

    if (password === '') {
      setPasswordError('Password cannot be empty');
      valid = false;
    } else {
      setPasswordError('');
    }

    if (valid) {
      // Proceed with form submission
      console.log('Form submitted');
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="bg-white p-8 rounded shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold text-blue-600 mb-6 text-left">Log in</h2>
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
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="password">Password</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            {passwordError && <p className="text-red-500 text-sm mt-1">{passwordError}</p>}
          </div>
          <div className="mb-4 flex items-center justify-between">
            <label className="inline-flex items-center">
              <input className="form-checkbox text-blue-600" type="checkbox" />
              <span className="ml-2 text-gray-700">Remember me</span>
            </label>
            <a className="text-blue-600 hover:underline" href="/reset-password">Forgot password?</a>
          </div>
          <button className="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit">Login</button>
        </form>
        <p className="text-center text-gray-600 mt-6">Don't have an account? <a href="/signup" className="text-blue-500 hover:underline font-semibold">Sign up</a></p>
      </div>
    </div>
  );
};

export default LoginForm;
