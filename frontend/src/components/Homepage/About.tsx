import React from 'react';

const About: React.FC = () => {
  return (
    <div className="container mx-auto p-8 flex flex-col md:flex-row items-center" id="about">
      <div className="md:w-1/2 mb-8 md:mb-0">
        <h1 className="text-5xl font-bold text-blue-600 mb-4">Helping students succeed!</h1>
        <h2 className="text-3xl font-semibold mb-4">Find equivalent community college courses</h2>
        <p className="text-2xl mb-6">TransferMax assists college students in saving time and money by identifying courses equivalent to those offered at community colleges.</p>
      </div>
      <div className="md:w-1/2 md:ml-12"> {/* Increased margin to md:ml-12 */}
        <img src="https://images.prismic.io/element451/1379a91d-d771-4d2c-af88-1394902912a3_Student+Success.jpg?auto=format&ixlib=react-9.0.3&h=600&w=800" alt="Student working on laptop" className="rounded shadow-lg" />
      </div>
    </div>
  );
};

export default About;
