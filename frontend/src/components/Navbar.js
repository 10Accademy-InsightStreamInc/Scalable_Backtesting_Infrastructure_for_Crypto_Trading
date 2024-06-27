import React, { useState, useEffect } from 'react';
import { useFormik } from 'formik';
import { Link, useLocation, useNavigate } from 'react-router-dom';

function Navbar() {
  const location = useLocation();
  const navigate = useNavigate();
  const [user_name, setUserName] = React.useState('');
  const currentPath = location.pathname;

  const fetchUserProfile = async () => {

    try {
      const token = localStorage.getItem('token');
      const response = await fetch('http://127.0.0.1:8000/auth/users/me', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch user profile');
      }

      const data = await response.json();
      console.log("The data from navbar :: ", data)
      setUserName(data.full_name);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchUserProfile();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="navbar bg-base-300">
      <div className="flex-1">
        <Link to="/" className="btn btn-ghost normal-case text-xl">{user_name}</Link>
      </div>
      <div className="flex-none">
        {currentPath === '/login' && <Link to="/signup" className="btn btn-outline">Sign Up</Link>}
        {currentPath === '/signup' && <Link to="/login" className="btn btn-outline">Login</Link>}
        {currentPath === '/backtest' && <Link to="/profile" className="btn btn-outline ml-2">Profile</Link>}
        {(currentPath === '/backtest' || currentPath === '/profile') && (
          <button onClick={handleLogout} className="btn btn-outline ml-2">Logout</button>
        )}
      </div>
    </div>
  );
}

export default Navbar;
