import React from 'react';

const Usage: React.FC = () => {
  return (
    <div className="bg-blue-900 text-white py-12" id="usage">
      <div className="container mx-auto px-4">
        <h1 className="text-3xl font-semibold mb-8 text-center">Get personalized transfer results in 3 easy steps!</h1>
        <div className="flex flex-col items-center w-full">
          <div className="flex flex-col md:flex-row justify-center space-y-8 md:space-y-0 md:space-x-8 mb-8 w-full">
            <div className="bg-white text-blue-900 p-8 rounded-lg shadow-lg flex-1 text-left">
              <h2 className="text-5xl font-bold mb-4">1</h2>
              <h3 className="text-2xl font-semibold mb-2">Create a free TransferMax account</h3>
              <p className="text-lg">Sign up quickly with an email address and fill in your profile.</p>
            </div>
            <div className="bg-white text-blue-900 p-8 rounded-lg shadow-lg flex-1 text-left">
              <h2 className="text-5xl font-bold mb-4">2</h2>
              <h3 className="text-2xl font-semibold mb-2">Add Courses</h3>
              <p className="text-lg">Add the college courses you have plan to take to your Courses schedule.</p>
            </div>
            <div className="bg-white text-blue-900 p-8 rounded-lg shadow-lg flex-1 text-left">
              <h2 className="text-5xl font-bold mb-4">3</h2>
              <h3 className="text-2xl font-semibold mb-2">View Results</h3>
              <p className="text-lg">See how much money will be saved at community colleges. Get more information and contact school staff.</p>
            </div>
          </div>
          <div className="bg-white text-blue-900 p-6 rounded-lg shadow-lg flex items-center w-full mb-8">
            <i className="fas fa-chart-bar text-4xl mr-4"></i>
            <p className="text-xl">Based on the schedule you provide, we look up our database for the cheapest equivalent community college courses to help you save the most money!</p>
          </div>
        </div>
        <div className="flex flex-col md:flex-row justify-between w-full max-w-7xl mx-auto mb-8">
          <div className="text-left w-full md:w-1/2 pr-0 md:pr-8 mb-8 md:mb-0">
            <h4 className="text-xl font-semibold mb-2">Note about match results</h4>
            <p className="text-lg mb-4 text-justify">The course equivalencies listed in TransferMax are accurate but may satisfy different degree requirements depending upon your major or program. Institutions may change the transfer information in TransferMax at any time, so be sure to contact them to verify how your courses will transfer.</p>
          </div>
          <div className="text-left w-full md:w-1/2 pl-0 md:pl-8">
            <h4 className="text-xl font-semibold mb-2">We recommend that you...</h4>
            <ul className="list-disc list-inside text-lg">
              <li>Contact advisors at the institutions to review your coursework for next steps</li>
              <li>Check TransferMax for updates</li>
              <li>Retain records of TransferMax reports for documentation</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Usage;
