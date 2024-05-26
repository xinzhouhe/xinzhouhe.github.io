import React from "react";

const DashboardHeader = () => {
    return (
        <div className="dashboard-header">
            <div>
                <h3 className="text-lg font-semibold">
                    Old Total Price
                </h3>
                <p className="text-2xl font-bold">
                    $190,000
                </p>
            </div>
            <div className="bg-yellow-100 p-4 rounded-lg shadow-lg transform transition duration-500 hover:scale-105">
                <h3 className="text-lg font-semibold text-yellow-800">
                    Student's Semester Savings
                </h3>
                <p className="text-4xl font-extrabold text-yellow-900">
                    $5,982
                </p>
                <p className="text-lg font-semibold text-yellow-700">
                    Save
                    <span className="text-5xl font-extrabold text-red-500">
                        30%
                    </span>
                    with TransferMax!
                </p>
            </div>
            <div>
                <h3 className="text-lg font-semibold">
                    New Total Price
                </h3>
                <p className="text-2xl font-bold">
                    $184,018
                </p>
            </div>
        </div>
    );
}

export default DashboardHeader;
