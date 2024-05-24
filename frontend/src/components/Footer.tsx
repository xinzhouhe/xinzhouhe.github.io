import React from 'react';

const Footer: React.FC = () => {
  return (
    <div className="bg-black text-white">
      <footer className="py-10">
        <div className="container mx-auto flex justify-between items-start">
          <div>
            <div className="flex items-center mb-4">
              <a href="../index.html">
                <span className="text-2xl font-bold">TransferMax</span>
              </a>
            </div>
            <p className="text-gray-400">Save money on tuition by finding the cheapest equivalent courses at community colleges.</p>
          </div>
          <div>
            <h3 className="text-gray-400 font-bold mb-2">QUICK LINKS</h3>
            <ul>
              <li className="mb-2"><a href="./index.html" className="text-gray-400 hover:text-white">Home</a></li>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">Privacy Policy</a></li>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">Accessibility</a></li>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">Terms of Use</a></li>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">FAQ</a></li>
            </ul>
          </div>
          <div>
            <h3 className="text-gray-400 font-bold mb-2">CONNECT</h3>
            <ul>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">Facebook</a></li>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">Instagram</a></li>
              <li className="mb-2"><a href="#" className="text-gray-400 hover:text-white">YouTube</a></li>
            </ul>
          </div>
        </div>
        <div className="text-center text-gray-400 mt-10">TransferMax © 2024</div>
      </footer>
    </div>
  );
};

export default Footer;
