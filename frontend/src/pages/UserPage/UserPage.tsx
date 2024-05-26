import React, { useState, useEffect } from 'react';
import './UserPage.css';
import Dashboard from '../../components/Dashboard/Dashboard';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UserPage: React.FC = () => {
  const [name, setName] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        console.error('No token found');
        return;
      }

      try {
        const response = await axios.get('http://localhost:5000/students/me', {
          headers: {
            Authorization: `Bearer ${token}`
          },
          withCredentials: true
        });
        if (response.status === 200) {
          const data = response.data;
          setName(data.name); // Assuming the response has a "name" field
        }
      } catch (error) {
        console.error('Failed to fetch user data', error);
      }
    };

    fetchUserData();
  }, []);

  const handleLogout = async () => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      console.error('No token found');
      return;
    }

    try {
      await axios.post('http://localhost:5000/auth/logout', {}, {
        headers: {
          Authorization: `Bearer ${token}`
        },
        withCredentials: true
      });

      // Clear the token and navigate to the login page
      localStorage.removeItem('accessToken');
      navigate('/login');
    } catch (error) {
      console.error('Failed to logout', error);
    }
  };

  return (
    <div className="userpage">
      <header className="bg-white shadow-md">
        <div className="container mx-auto flex justify-between items-center py-4 px-6">
          <div className="flex items-center">
            <a href="#">
              <img
                alt="Logo of TransferMax with a stylized graduation cap and dollar sign"
                height="100"
                src="https://cdn.b12.io/client_media/lC4B07wH/3d38abd0-1661-11ef-8efb-0242ac110002-dc907157a60bfff1db2be84d6f8d489.png"
                width="300"
              />
            </a>
          </div>
          <nav className="space-x-4 flex items-center">
            <div className="relative dropdown">
              <button className="bg-blue-600 text-white px-4 py-2 rounded-full hover:bg-blue-700 flex items-center">
                <i className="fa fa-user mr-2"></i>
                {name ? <span>{name}</span> : <span>Loading...</span>}
              </button>
              <div className="dropdown-menu">
                <a className="edit-profile" href="#">
                  Edit Profile
                </a>
                <a className="logout" href="#" onClick={handleLogout}>
                  Log Out
                </a>
              </div>
            </div>
          </nav>
        </div>
      </header>
      <div className="content">
        <Dashboard />
      </div>
      <div className="bg-black text-white">
        <footer className="py-10">
          <div className="container mx-auto flex justify-between items-start">
            <div>
              <div className="flex items-center mb-4">
                <a href="#">
                  <span className="text-2xl font-bold">TransferMax</span>
                </a>
              </div>
              <p className="text-gray-400">
                Save money on tuition by finding the cheapest equivalent courses at community colleges.
              </p>
            </div>
            <div>
              <h3 className="text-gray-400 font-bold mb-2">QUICK LINKS</h3>
              <ul>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    Home
                  </a>
                </li>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    Privacy Policy
                  </a>
                </li>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    Accessibility
                  </a>
                </li>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    Terms of Use
                  </a>
                </li>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    FAQ
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="text-gray-400 font-bold mb-2">CONNECT</h3>
              <ul>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    Facebook
                  </a>
                </li>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    Instagram
                  </a>
                </li>
                <li className="mb-2">
                  <a className="text-gray-400 hover:text-white" href="#">
                    YouTube
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div className="text-center text-gray-400 mt-10">TransferMax © 2024</div>
        </footer>
      </div>
    </div>
  );
};

export default UserPage;
