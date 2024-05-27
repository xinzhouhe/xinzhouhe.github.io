import React from "react";

const DashboardTable = () => {
    const calculateOldPrice = (newPrice: number) => {
        return (newPrice / 0.70).toFixed(2);
    };

    const courses = [
        { original: "English 101", genEd: "English", credits: 3, equivalent: "Eng 234", newPrice: 325, online: "Y" },
        { original: "Math 101", genEd: "Mathematics", credits: 4, equivalent: "Math 201", newPrice: 400, online: "Y" },
        { original: "History 101", genEd: "History", credits: 3, equivalent: "Hist 202", newPrice: 350, online: "N" },
    ];

    return (
        <table className="dashboard-table">
            <thead>
                <tr>
                    <th>Original Course (University of Delaware)</th>
                    <th>Gen Ed Requirement</th>
                    <th>Old Price</th>
                    <th>Credits</th>
                    <th>Equivalent Course (Rutgers New Brunswick)</th>
                    <th>New Price</th>
                    <th>Online</th>
                </tr>
            </thead>
            <tbody>
                {courses.map((course, index) => (
                    <tr key={index}>
                        <td>{course.original}</td>
                        <td>{course.genEd}</td>
                        <td>${calculateOldPrice(course.newPrice)}</td>
                        <td>{course.credits}</td>
                        <td>{course.equivalent}</td>
                        <td>${course.newPrice}</td>
                        <td>{course.online}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default DashboardTable;
