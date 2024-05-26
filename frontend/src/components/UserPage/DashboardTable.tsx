import React from "react";

const DashboardTable = () => {
    return (
        <table className="dashboard-table">
                <thead>
                    <tr>
                        <th>
                            Original Course
                        </th>
                        <th>
                            Gen Ed Requirement
                        </th>
                        <th>
                            Credits
                        </th>
                        <th>
                            Equivalent Course
                        </th>
                        <th>
                            New Price
                        </th>
                        <th>
                            Online
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            English 101
                        </td>
                        <td>
                            English
                        </td>
                        <td>
                            3
                        </td>
                        <td>
                            Eng 234
                        </td>
                        <td>
                            $325
                        </td>
                        <td>
                            Y
                        </td>
                    </tr>
                    <tr>
                        <td>
                            Math 101
                        </td>
                        <td>
                            Mathematics
                        </td>
                        <td>
                            4
                        </td>
                        <td>
                            Math 201
                        </td>
                        <td>
                            $400
                        </td>
                        <td>
                            Y
                        </td>
                    </tr>
                    <tr>
                        <td>
                            History 101
                        </td>
                        <td>
                            History
                        </td>
                        <td>
                            3
                        </td>
                        <td>
                            Hist 202
                        </td>
                        <td>
                            $350
                        </td>
                        <td>
                            N
                        </td>
                    </tr>
                </tbody>
            </table>
    )
}

export default DashboardTable;