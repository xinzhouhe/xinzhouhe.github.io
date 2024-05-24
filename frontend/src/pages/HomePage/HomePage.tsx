import React from 'react';
import Header from '../../components/Utils/Header';
import Navbar from '../../components/Homepage/Navbar';
import Main from '../../components/Homepage/Main';
import About from '../../components/Homepage/About';
import Usage from '../../components/Homepage/Usage';
import Contact from '../../components/Homepage/Contact';
import Footer from '../../components/Utils/Footer';
import './HomePage.css';
import { Helmet } from 'react-helmet';

const Home: React.FC = () => {
  return (
    <div className="Home">
      <Helmet>
        <title>TransferMax - Home</title>
      </Helmet>
      <div className="fixed top-0 left-0 w-full z-50">
        <header className="bg-white shadow-md">
          <div className="container mx-auto flex justify-between items-center py-4 px-6">
            <Header />
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
