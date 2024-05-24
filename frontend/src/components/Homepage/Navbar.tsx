// src/components/Navbar.tsx
import React from 'react';
import { Link } from 'react-scroll';

const Navbar: React.FC = () => {
  return (
    <nav className="bg-blue-600">
      <div className="container mx-auto flex justify-center space-x-6 py-3">
        <Link
          to="home"
          smooth={true}
          duration={500}
          className="text-white font-semibold text-lg nav-link cursor-pointer"
        >
          Home
        </Link>
        <Link
          to="about"
          smooth={true}
          duration={500}
          className="text-white font-semibold text-lg nav-link cursor-pointer"
        >
          About
        </Link>
        <Link
          to="usage"
          smooth={true}
          duration={500}
          className="text-white font-semibold text-lg nav-link cursor-pointer"
        >
          Usage
        </Link>
        <Link
          to="contact"
          smooth={true}
          duration={500}
          className="text-white font-semibold text-lg nav-link cursor-pointer"
        >
          Contact
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
