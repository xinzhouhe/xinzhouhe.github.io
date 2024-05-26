import React from "react";
import DashboardHeader from "./DashboardHeader";
import DashboardActions from "./DashboardActions";
import DashboardTable from "./DashboardTable";

const Dashboard: React.FC = () => {
    return (
        <div className="main-content container mx-auto flex flex-col py-6 px-6">
            <DashboardHeader />
            <div className="flex-grow">
                <DashboardTable />
            </div> {/* This div will push the actions to the bottom */}
            <DashboardActions />
        </div>
    );
};

export default Dashboard;