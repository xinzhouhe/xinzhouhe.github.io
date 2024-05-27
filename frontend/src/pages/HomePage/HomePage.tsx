import React, { useEffect, useState } from 'react';
import Header from '../../components/Utils/Header';
import Navbar from '../../components/Homepage/Navbar';
import Main from '../../components/Homepage/Main';
import About from '../../components/Homepage/About';
import Usage from '../../components/Homepage/Usage';
import axios from 'axios';
import Contact from '../../components/Homepage/Contact';
import Footer from '../../components/Utils/Footer';
import { Helmet } from 'react-helmet';
import './HomePage.css';

const Home: React.FC = () => {
  const [isAccessTokenRemoved, setIsAccessTokenRemoved] = useState<boolean>(false);
  const [name, setName] = useState<string | null>(null);

  useEffect(() => {
    console.log("inside home page: " + localStorage.getItem('accessToken'));
    const tokenRemoved = localStorage.getItem('accessToken') === null;
    setIsAccessTokenRemoved(tokenRemoved);

    if (!tokenRemoved) {
      // If the access token is not removed, fetch the user's name
      const fetchUserName = async () => {
        try {
          const accessToken = localStorage.getItem('accessToken');
          if (accessToken) {
            const response = await axios.get('http://localhost:5000/students/me', {
              headers: {
                Authorization: `Bearer ${accessToken}`,
              },
              withCredentials: true
            });
            setName(response.data.name);
          }
        } catch (error) {
          console.error('Error fetching user data:', error);
        }
      };

      fetchUserName();
    }
  }, []);

  return (
    <div className="Home">
      <Helmet>
        <title>TransferMax - Home</title>
      </Helmet>
      <div className="fixed top-0 left-0 w-full z-50">
        <header className="bg-white shadow-md">
          <div className="container mx-auto flex justify-between items-center py-4 px-6">
            <Header />
            { !isAccessTokenRemoved ? (
              <nav className="space-x-4 flex items-center">
                <div className="relative dropdown">

                  <button className="bg-blue-600 text-white px-4 py-2 rounded-full hover:bg-blue-700 flex items-center">

                    <i className="fa fa-user mr-2"></i>
                    {name ? <span>{name}</span> : <span>Loading...</span>}
                  </button>
                  <div className="dropdown-menu">
                    <a className="edit-profile block px-4 py-2 text-gray-800 hover:bg-gray-100" href="/">
                      Edit Profile
                    </a>
                    <a
                      className="logout block px-4 py-2 text-gray-800 hover:bg-gray-100"
                      href="/"
                      onClick={() => {
                        localStorage.removeItem('accessToken');
                        setIsAccessTokenRemoved(true);
                      }}
                    >
                      Log Out
                    </a>
                  </div>
                </div>
              </nav>
            ) : (
              <nav className="space-x-4">
                <a className="hover:underline text-blue-600 font-semibold text-lg" href="/login">
                  Log in
                </a>
                <a
                  className="bg-green-500 text-white px-4 py-2 rounded-full font-semibold text-lg hover:bg-green-600"
                  href="/signup"
                >
                  Sign up
                </a>
              </nav>
            )}
          </div>
        </header>
        <Navbar />
      </div>
      <div id="home" className="pt-32">
        <Main />
      </div>
      <div id="about" className="pt-32">
        <About />
      </div>
      <div id="usage" className="pt-32">
        <Usage />
      </div>
      <div id="contact" className="pt-32">
        <Contact />
      </div>
      <Footer />
    </div>
  );
};

export default Home;