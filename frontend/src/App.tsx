// src/App.tsx
import React from 'react';
import Header from './components/Header';
import Navbar from './components/Navbar';
import Main from './components/Main';
import About from './components/About';
import Usage from './components/Usage';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './index.css';

const App: React.FC = () => {
  return (
    <div className="App">
      <div className="fixed top-0 left-0 w-full z-50">
        <header className="bg-white shadow-md">
          <div className="container mx-auto flex justify-between items-center py-4 px-6">
            <Header />
            <nav className="space-x-4">
              <a className="hover:underline text-blue-600 font-semibold text-lg" href="./login.html">
                Log in
              </a>
              <a
                className="bg-green-500 text-white px-4 py-2 rounded-full font-semibold text-lg hover:bg-green-600"
                href="./signup.html"
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
      <div id="about" className="pt-16">
        <About />
      </div>
      <div id="usage" className="pt-16">
        <Usage />
      </div>
      <div id="contact" className="pt-16">
        <Contact />
      </div>
      <Footer />
    </div>
  );
};

export default App;
