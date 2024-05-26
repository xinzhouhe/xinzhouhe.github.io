import React from 'react';

const DashboardActions: React.FC = () => {
    return (
        <div className="dashboard-actions container mx-auto flex justify-between p-4 bg-e0f7fa rounded-lg shadow-md sticky bottom-0 z-10">
            <button className="share bg-00796b text-white px-4 py-2 rounded-full hover:bg-004d40 flex items-center">
                <i className="fas fa-share mr-2"></i>
                Share
            </button>
            <button className="add-course bg-00796b text-white px-4 py-2 rounded-full hover:bg-004d40 flex items-center">
                <i className="fas fa-plus mr-2"></i>
                Add New Course
            </button>
            <button className="export bg-00796b text-white px-4 py-2 rounded-full hover:bg-004d40 flex items-center">
                <i className="fas fa-file-export mr-2"></i>
                Export
            </button>
        </div>
    );
};

export default DashboardActions;
