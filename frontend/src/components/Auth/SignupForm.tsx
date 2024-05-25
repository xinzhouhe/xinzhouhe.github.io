import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SignupForm: React.FC = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [registerError, setRegisterError] = useState('');
  const [registerSuccess, setRegisterSuccess] = useState('');

  const navigate = useNavigate();

  const validateEmail = (email: string) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    let valid = true;
    let newErrors = {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      confirmPassword: ''
    };

    if (firstName === '') {
      newErrors.firstName = 'First name cannot be empty';
      valid = false;
    }
    if (lastName === '') {
      newErrors.lastName = 'Last name cannot be empty';
      valid = false;
    }
    if (email === '') {
      newErrors.email = 'Email cannot be empty';
      valid = false;
    } else if (!validateEmail(email)) {
      newErrors.email = 'Email is not valid';
      valid = false;
    }
    if (password === '') {
      newErrors.password = 'Password cannot be empty';
      valid = false;
    }
    if (confirmPassword === '') {
      newErrors.confirmPassword = 'Confirm password cannot be empty';
      valid = false;
    } else if (password !== confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
      valid = false;
    }

    setErrors(newErrors);

    if (valid) {
      // Proceed with form submission
      try {
        const response = await axios.post('http://localhost:5000/auth/register', {
          name: `${firstName} ${lastName}`,
          email,
          password,
          university_id: null,
          state: '',
          us_citizen: null,
        });

        if (response.status === 201) {
          setRegisterSuccess('Student registered successfully');
          setRegisterError('');

          // Redirect to the login page after a short delay
          setTimeout(() => {
            navigate('/login');
          }, 2000); // 2 seconds delay
        } else {
          setRegisterError('Registration failed');
        }
      } catch (error) {
        if (axios.isAxiosError(error) && error.response) {
          if (error.response.status === 400 && error.response.data.message === 'Email already exists') {
            setRegisterError('Email already exists');
          } else {
            setRegisterError(error.response.data.message);
          }
        } else {
          setRegisterError('An error occurred. Please try again.');
        }
        setRegisterSuccess('');
      }
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="bg-white p-8 rounded shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold text-green-600 mb-6 text-left">Sign Up</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="first-name">First Name</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="first-name"
              type="text"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
            {errors.firstName && <p className="text-red-500 text-sm mt-1">{errors.firstName}</p>}
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="last-name">Last Name</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="last-name"
              type="text"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
            {errors.lastName && <p className="text-red-500 text-sm mt-1">{errors.lastName}</p>}
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="email">Email address</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email}</p>}
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
            {errors.password && <p className="text-red-500 text-sm mt-1">{errors.password}</p>}
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="confirm-password">Confirm Password</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="confirm-password"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
            {errors.confirmPassword && <p className="text-red-500 text-sm mt-1">{errors.confirmPassword}</p>}
          </div>
          {registerError && <p className="text-red-500 text-sm mb-4">{registerError}</p>}
          {registerSuccess && <p className="text-green-500 text-sm mb-4">{registerSuccess}</p>}
          <button className="w-full bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-green-600" type="submit">Sign Up</button>
        </form>
        <p className="text-center text-gray-600 mt-6">Already have an account? <a href="/login" className="text-green-600 hover:underline font-semibold">Log in</a></p>
      </div>
    </div>
  );
};

export default SignupForm;
