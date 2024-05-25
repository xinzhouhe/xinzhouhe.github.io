import React from 'react';
import './Dashboard.css';

const Dashboard: React.FC = () => {
  return (
    <div className="main-content container mx-auto py-8">
      <div className="dashboard-header">
        <div>
          <h3 className="text-lg font-semibold">Old Total Price</h3>
          <p className="text-2xl font-bold">$190,000</p>
        </div>
        <div className="bg-yellow-100 p-4 rounded-lg shadow-lg transform transition duration-500 hover:scale-105">
          <h3 className="text-lg font-semibold text-yellow-800">Student's Semester Savings</h3>
          <p className="text-4xl font-extrabold text-yellow-900">$5,982</p>
          <p className="text-lg font-semibold text-yellow-700">
            Save <span className="text-5xl font-extrabold text-red-500">30%</span> with TransferMax!
          </p>
        </div>
        <div>
          <h3 className="text-lg font-semibold">New Total Price</h3>
          <p className="text-2xl font-bold">$184,018</p>
        </div>
      </div>
      <table className="dashboard-table">
        <thead>
          <tr>
            <th>Original Course</th>
            <th>Gen Ed Requirement</th>
            <th>Credits</th>
            <th>Equivalent Course</th>
            <th>New Price</th>
            <th>Online</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>English 101</td>
            <td>English</td>
            <td>3</td>
            <td>Eng 234</td>
            <td>$325</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Math 101</td>
            <td>Mathematics</td>
            <td>4</td>
            <td>Math 201</td>
            <td>$400</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>History 101</td>
            <td>History</td>
            <td>3</td>
            <td>Hist 202</td>
            <td>$350</td>
            <td>N</td>
          </tr>
          <tr>
            <td>Biology 101</td>
            <td>Science</td>
            <td>4</td>
            <td>Bio 203</td>
            <td>$450</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Psychology 101</td>
            <td>Social Science</td>
            <td>3</td>
            <td>Psy 204</td>
            <td>$300</td>
            <td>N</td>
          </tr>
          <tr>
            <td>Art 101</td>
            <td>Arts</td>
            <td>3</td>
            <td>Art 205</td>
            <td>$375</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Physics 101</td>
            <td>Science</td>
            <td>4</td>
            <td>Phys 206</td>
            <td>$500</td>
            <td>N</td>
          </tr>
          <tr>
            <td>Chemistry 101</td>
            <td>Science</td>
            <td>4</td>
            <td>Chem 207</td>
            <td>$480</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Philosophy 101</td>
            <td>Humanities</td>
            <td>3</td>
            <td>Phil 208</td>
            <td>$320</td>
            <td>N</td>
          </tr>
          <tr>
            <td>Economics 101</td>
            <td>Social Science</td>
            <td>3</td>
            <td>Econ 209</td>
            <td>$310</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Computer Science 101</td>
            <td>Technology</td>
            <td>4</td>
            <td>CS 210</td>
            <td>$450</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Music 101</td>
            <td>Arts</td>
            <td>3</td>
            <td>Mus 211</td>
            <td>$370</td>
            <td>N</td>
          </tr>
          <tr>
            <td>Geography 101</td>
            <td>Social Science</td>
            <td>3</td>
            <td>Geo 212</td>
            <td>$340</td>
            <td>Y</td>
          </tr>
          <tr>
            <td>Sociology 101</td>
            <td>Social Science</td>
            <td>3</td>
            <td>Soc 213</td>
            <td>$330</td>
            <td>N</td>
          </tr>
          <tr>
            <td>Anthropology 101</td>
            <td>Social Science</td>
            <td>3</td>
            <td>Anth 214</td>
            <td>$360</td>
            <td>Y</td>
          </tr>
        </tbody>
      </table>
      <div className="dashboard-actions container mx-auto">
        <button className="share">
          <i className="fa fa-share"></i> Share
        </button>
        <button className="add-course">
          <i className="fa fa-plus"></i> Add New Course
        </button>
        <button className="export">
          <i className="fa fa-file-export"></i> Export
        </button>
      </div>
    </div>
  );
};

export default Dashboard;
