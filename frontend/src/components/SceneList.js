import React, { useState, useEffect } from 'react';
import { FaList, FaEye, FaSpinner, FaExclamationCircle } from 'react-icons/fa';
// import 'tailwindcss/tailwind.css';

function ScenesList() {
  const [scenes, setScenes] = useState([]);
  const [selectedScene, setSelectedScene] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [bestBacktest, setBestBacktest] = useState(null);

  useEffect(() => {
    const fetchScenes = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8001/scenes/');
        if (!response.ok) throw new Error('Error fetching scenes');
        const data = await response.json();
        setScenes(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchScenes();
  }, []);

  const handleSceneClick = async (sceneId) => {
    setLoading(true);
    setError(null);

    try {
      // fetch from two different endpoints
      const response = await fetch(`http://127.0.0.1:8001/scenes/${sceneId}`);
      if (!response.ok){
        const err = await response.text();
        throw new Error('Error fetching scene details', err);
      }
      const data = await response.json();
      console.log("The Data from SceneList id77 :: ",data);
      setSelectedScene(data);

      const response2 = await fetch(`http://127.0.0.1:8001/best_indicator/${sceneId}`);
      if (!response2.ok) throw new Error('Error fetching best backtest');
      const data2 = await response2.json();
      console.log("The Data from SceneList Best Backtest is :: ",data2);
      setBestBacktest(data2);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4 flex items-center">
        <FaList className="mr-2" /> Scenes List
      </h1>

      {error && (
        <div className="alert alert-error bg-red-100 border-l-4 border-red-500 text-red-700 p-4" role="alert">
          <FaExclamationCircle className="mr-2" />
          <span>{error}</span>
        </div>
      )}

      <ul className="space-y-4">
        {scenes.map((scene) => (
          <li key={scene.id} className="bg-gray-800 shadow-md rounded-lg p-4 hover:bg-gray-100 transition duration-200">
            <button
              onClick={() => handleSceneClick(scene.id)}
              className="flex items-center w-full text-left focus:outline-none"
            >
              <FaEye className="text-blue-500 mr-2" />
              <span>Scene {scene.id}: {scene.start_date} to {scene.end_date}</span>
            </button>
          </li>
        ))}
      </ul>

      {loading && (
        <div className="flex justify-center items-center mt-4">
          <FaSpinner className="animate-spin text-blue-500 text-2xl" />
          <span className="ml-2">Loading scene details...</span>
        </div>
      )}

      {selectedScene && (
        <div className="mt-8 bg-gray-700 shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Scene Details</h2>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <p><strong>Period:</strong> {selectedScene.period}</p>
              <p><strong>Stock:</strong> {selectedScene.stock.name}</p>
            </div>
          </div>

          <h3 className="text-lg font-semibold mt-6">Backtests</h3>
          <ul className="space-y-4">
            {selectedScene.backtests.map((backtest) => (
              // show the best backtest with green background bestBacktest
              <li
                key={backtest.id}
                className={`bg-gray-600 p-4 rounded-lg shadow-md ${backtest.id === bestBacktest?.id ? 'bg-green-900' : ''}`}
              >
                <p><strong>Initial Cash:</strong> ${backtest.initial_cash.toFixed(2)}</p>
                <p><strong>Indicator:</strong> {backtest.indicator.name}</p>
                <p><strong>Final Value:</strong> ${backtest.final_value.toFixed(2)}</p>
                <p><strong>Sharpe Ratio:</strong> {backtest.sharpe_ratio}</p>
                <p><strong>Losing Trades:</strong> {backtest.losing_trades}</p>
                <p><strong>Winning Trades:</strong> {backtest.winning_trades}</p>
                <p><strong>Total Trades:</strong> {backtest.total_trades}</p>
                <p><strong>Max Drawdown:</strong> {backtest.max_drawdown?.toFixed(2)}%</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ScenesList;
