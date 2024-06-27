import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';

function Navbar() {
  const location = useLocation();
  const navigate = useNavigate();
  const currentPath = location.pathname;

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="navbar bg-base-300">
      <div className="flex-1">
        <Link to="/" className="btn btn-ghost normal-case text-xl">Crypto Data Pipeline</Link>
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
