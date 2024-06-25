import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import BacktestForm from './components/BacktestForm';
import Signup from './components/Signup';
import Login from './components/Login';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="container mx-auto p-4">
          <Routes>
            <Route path="/" element={<Navigate to="/login" />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/backtest" element={<BacktestForm />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
