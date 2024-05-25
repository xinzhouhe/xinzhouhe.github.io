import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import axios from 'axios';

const ResetPwdForm: React.FC = () => {
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [resetError, setResetError] = useState('');
  const [resetSuccess, setResetSuccess] = useState('');
  const navigate = useNavigate();
  const location = useLocation();

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    const query = new URLSearchParams(location.search);
    const token = query.get('token');

    if (!token) {
      setResetError('Invalid or missing token');
      return;
    }

    if (newPassword === '' || confirmPassword === '') {
      setPasswordError('Passwords cannot be empty');
      return;
    } else if (newPassword !== confirmPassword) {
      setPasswordError('Passwords do not match');
      return;
    } else {
      setPasswordError('');
    }

    try {
      const response = await axios.post(`http://localhost:5000/auth/reset_password/${token}`, { newPassword });

      if (response.status === 200) {
        setResetSuccess('Password reset successfully!');
        setTimeout(() => {
          navigate('/login');
        }, 2000); // 2秒后跳转到登录页面
      } else {
        setResetError('Failed to reset password');
      }
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        setResetError(error.response.data.message);
      } else {
        setResetError('An error occurred. Please try again.');
      }
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="bg-white p-8 rounded shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold text-blue-600 mb-6 text-center">Change Your Password</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="new-password">New Password</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="new-password"
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 font-bold mb-2" htmlFor="confirm-password">Confirm New Password</label>
            <input
              className="w-full px-3 py-2 border border-gray-300 rounded"
              id="confirm-password"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </div>
          {passwordError && <p className="text-red-500 text-sm mb-4">{passwordError}</p>}
          {resetError && <p className="text-red-500 text-sm mb-4">{resetError}</p>}
          {resetSuccess && <p className="text-green-500 text-sm mb-4">{resetSuccess}</p>}
          <button className="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit">Reset Password</button>
        </form>
      </div>
    </div>
  );
};

export default ResetPwdForm;
