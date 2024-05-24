// src/components/Header.tsx
import React from 'react';

const Header: React.FC = () => {
  return (
    <div className="flex items-center">
      <a href="../index.html">
        <img
          src="https://cdn.b12.io/client_media/lC4B07wH/3d38abd0-1661-11ef-8efb-0242ac110002-dc907157a60bfff1db2be84d6f8d489.png"
          width="300"
          alt="Logo"
          className="mr-3"
        />
      </a>
    </div>
  );
};

export default Header;
