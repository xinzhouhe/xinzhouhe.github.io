import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LoginForm: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [loginError, setLoginError] = useState('');

  useEffect(() => {
    const rememberedEmail = localStorage.getItem('rememberedEmail');
    if (rememberedEmail) {
      setEmail(rememberedEmail);
      setRememberMe(true);
    }
  }, []);

  const navigate = useNavigate();

  const validateEmail = (email: string) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const handleSubmit = async (event: React.FormEvent) => {
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
      // Make the API call to log in using axios
      try {
        const response = await axios.post('http://localhost:5000/auth/login', {
          email,
          password,
        });

        if (response.status === 200) {
          const data = response.data;
          console.log('Login successful', data);
          // You can now store the access token in local storage or a context/state management library
          localStorage.setItem('accessToken', data.access_token);
          localStorage.setItem('is_login', 'true'); // Set is_login variable

          // Handle "Remember Me" functionality
          if (rememberMe) {
            localStorage.setItem('rememberedEmail', email);
          } else {
            localStorage.removeItem('rememberedEmail');
          }
          setLoginError('');

          // Redirect to another page after successful login
          setTimeout(() => {
            if (data.is_first_login) {
              navigate('/user/edit-profile');
            } else {
              navigate('/user/dashboard');
            }
          }, 2000); // 2 seconds delay
        }
      } catch (error) {
        if (axios.isAxiosError(error) && error.response) {
          setLoginError(error.response.data.message);
        } else {
          setLoginError('An error occurred. Please try again.');
        }

        // Reset all inputs on unsuccessful login
        setEmail('');
        setPassword('');
        setRememberMe(false);
      }
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
              <input
                className="form-checkbox text-blue-600"
                type="checkbox"
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
              />
              <span className="ml-2 text-gray-700">Remember me</span>
            </label>
            <a className="text-blue-600 hover:underline" href="/reset-password/send-link">Forgot password?</a>
          </div>
          {loginError && <p className="text-red-500 text-sm mb-4">{loginError}</p>}
          <button className="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit" >Login</button>
        </form>
        <p className="text-center text-gray-600 mt-6">Don't have an account? <a href="/signup" className="text-blue-500 hover:underline font-semibold">Sign up</a></p>
      </div>
    </div>
  );
};

export default LoginForm;
