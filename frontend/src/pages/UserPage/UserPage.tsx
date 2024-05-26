import React , { useState, useEffect } from 'react';
import Header from "../../components/Utils/Header";
import Footer from "../../components/Utils/Footer";
import Dashboard from "../../components/Dashboard/Dashboard";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import "./UserPage.css";

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
          navigate('/');
        } catch (error) {
          console.error('Failed to logout', error);
        }
      };

return (
    <div className="user-page">
        <div className="content-area">
            <header className="bg-white shadow-md">
                <div className="container mx-auto flex justify-between items-center py-4 px-6">
                    <Header />
                    <nav className="space-x-4 flex items-center">
                        <div className="relative dropdown">
                            <button className="bg-blue-600 text-white px-4 py-2 rounded-full hover:bg-blue-700 flex items-center">
                                <i className="fa fa-user mr-2"></i>
                                {name ? <span>{name}</span> : <span>Loading...</span>}
                            </button>
                            <div className="dropdown-menu">
                                <a className="edit-profile" href="/">
                                    Edit Profile
                                </a>
                                <a className="logout" onClick={handleLogout}>
                                    Log Out
                                </a>
                            </div>
                        </div>
                    </nav>
                </div>
            </header>
            <Dashboard />
            <div className="footer-container">
                <Footer />
            </div>
        </div>
    </div>
);
};

export default UserPage;
