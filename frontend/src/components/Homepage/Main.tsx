import React, { useEffect, useState } from 'react';

const Main: React.FC = () => {
  const [isLogin, setIsLogin] = useState(false);

  useEffect(() => {
    const loginStatus = localStorage.getItem('is_login') === 'true';
    setIsLogin(loginStatus);
  }, []);

  return (
    <main className="relative">
      <img 
        src="https://ccrc.tc.columbia.edu/images/manycauses.jpg" 
        alt="Community college research center" 
        className="w-full h-[40rem] object-cover" 
      />
      <div className="absolute inset-0 bg-black bg-opacity-50 flex flex-col justify-center items-center text-center text-white">
        <h2 className="text-6xl font-bold mb-4">TransferMax</h2>
        <p className="text-2xl mb-6">Simplify Your Course Transfers and Save Money</p>
        <a 
          href={isLogin ? "/user/dashboard" : "/signup"} 
          className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full text-xl"
        >
          {isLogin ? "My Dashboard" : "Get Started"}
        </a>
        {!isLogin && (
          <p className="text-lg mt-6">
            Have an account? <a href="/login" className="text-white semi-bold hover:underline font-semibold">Log in</a>
          </p>
        )}
      </div>
    </main>
  );
};

export default Main;
