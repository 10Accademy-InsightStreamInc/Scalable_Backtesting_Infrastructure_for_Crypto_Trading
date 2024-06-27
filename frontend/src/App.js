import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import BacktestForm from './components/BacktestForm';
import Signup from './components/Signup';
import Login from './components/Login';
import Profile from './components/Profile';
import ScenesList from './components/SceneList';

const PrivateRoute = ({ element: Element, ...rest }) => {
  const token = localStorage.getItem('token');
  return token ? <Element {...rest} /> : <Navigate to="/login" />;
};

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="container mx-auto p-4">
          <Routes>
            <Route path="/" element={<Navigate to="/login" />} />
            <Route path="/signup" element={<Signup />} />
            {/* if the user is already logged in and tries to see /login redirect to /scenes */}
            <Route path="/login" element={<Navigate to="/scenes" />} />
            <Route path="/signup" element={<Navigate to="/scenes" />} />
            <Route path="/login" element={<Login />} />
            <Route path="/scenes" element={<PrivateRoute element={ScenesList} />} />
            <Route path="/backtest" element={<PrivateRoute element={BacktestForm} />} />
            <Route path="/profile" element={<PrivateRoute element={Profile} />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
