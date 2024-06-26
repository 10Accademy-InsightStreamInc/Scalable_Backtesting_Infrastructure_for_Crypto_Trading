import React, { useState, useEffect } from 'react';

function BacktestForm() {
  const [parameters, setParameters] = useState({
    startDate: '',
    endDate: '',
    indicator: '',
    stock: '',
    paramsRange: '',
  });

  const [results, setResults] = useState(null);
  const [indicators, setIndicators] = useState([]);
  const [stocks, setStocks] = useState([]);
  const [stockDescription, setStockDescription] = useState('');
  const [indicatorDescription, setIndicatorDescription] = useState('');

  useEffect(() => {
    // Simulate fetching indicators and stocks from an API
    const fetchIndicators = async () => {
      const response = await fetch('http://127.0.0.1:8000/indicators/');
      const data = await response.json();
      console.log("The Response on Indicators is :: ",data);

      setIndicators(data);
    };

    const fetchStocks = async () => {
      const response = await fetch('http://127.0.0.1:8000/stocks/');
      const data = await response.json();
      console.log("The Response on Stocks is :: ",data);
      setStocks(data);
    };

    fetchIndicators();
    fetchStocks();
  }, []);

  const handleChange = (e) => {
    setParameters({
      ...parameters,
      [e.target.name]: e.target.value,
    });

    console.log("The changed s ::",e.target.name, "The Val =" ,e.target.value);

    if (e.target.name === 'stock') {
      console.log("It is here")
      const selectedStock = stocks.find(stock => stock.id === parseInt(e.target.value));
      console.log("Selected Stock :: ",selectedStock)
      setStockDescription(selectedStock ? selectedStock.description : '');
    }

    if (e.target.name === 'indicator') {
      const selectedIndicator = indicators.find(indicator => indicator.id === parseInt(e.target.value));
      setIndicatorDescription(selectedIndicator ? selectedIndicator.description : '');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(parameters);
    let a = {
      "period": 15,
      "start_date": parameters["startDate"],
      "end_date": parameters['endDate'],
      "indicator_id": parameters["indicator"], // 
      "stock_id": parameters["stock"] // Nvidia
   }
   console.log("The final to be sent to API is :: ", a)
    // API POST call to backend
    const response = await fetch('http://127.0.0.1:8000/scenes/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(a),
    });
    // const response = await fetch('https://localhost'); 
    // const response = {
    //   "return": "10%",
    //   "numberOfTrades": 50,
    //   "winningTrades": 30,
    //   "losingTrades": 20,
    //   "maxDrawdown": "5%",
    //   "sharpeRatio": 1.5
    // };
    const scene = await response.json()
    console.log("The Response of backtest is :: ",scene);

    const scene_id = scene.id;
    console.log("The Scene ID is :: ",scene_id);

    // const response2 = await fetch('http://127.0.0.1:8000//backtests/'+scene_id+'/');
    const response2 = await fetch('http://127.0.0.1:8000/backtests/'+scene_id+'/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(""),
    });

    const data2 = await response2.json();

    console.log("The Response of backtest is :: ",data2);
    
    // const data = await response.json();
    // const data = response;
    setResults(data2[0]);
  };

  return (
    <div className="card bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Backtest Parameters</h2>
        <form onSubmit={handleSubmit}>
          <div className="grid grid-cols-2 gap-4">
            <div className="form-control">
              <label className="label">
                <span className="label-text">Initial Cash</span>
              </label>
              <input
                type="text"
                name="paramsRange"
                value={parameters.paramsRange}
                onChange={handleChange}
                className="input input-bordered"
                placeholder="e.g., 1000, 2000,10,000"
                required
              />
            </div>

            <div className="form-control">
              <label className="label">
                <span className="label-text">Stock</span>
              </label>
              <select
                name="stock"
                value={parameters.stock}
                onChange={handleChange}
                className="select select-bordered"
                required
              >
                <option value="">Select a stock</option>
                {stocks.map((stock) => (
                  <option key={stock.id} value={stock.id}>
                    {stock.name}
                  </option>
                ))}
              </select>
              <small className="text-gray-500">{stockDescription}</small>
            </div>

            <div className="form-control">
              <label className="label">
                <span className="label-text">Start Date</span>
              </label>
              <input
                type="date"
                name="startDate"
                value={parameters.startDate}
                onChange={handleChange}
                className="input input-bordered"
                required
              />
            </div>

            <div className="form-control">
              <label className="label">
                <span className="label-text">End Date</span>
              </label>
              <input
                type="date"
                name="endDate"
                value={parameters.endDate}
                onChange={handleChange}
                className="input input-bordered"
                required
              />
            </div>

            <div className="col-span-2 form-control">
              <label className="label">
                <span className="label-text">Metric</span>
              </label>
              <select
                name="indicator"
                value={parameters.indicator}
                onChange={handleChange}
                className="select select-bordered"
                required
              >
                <option value="">Select a metric</option>
                {indicators.map((indicator) => (
                  <option key={indicator.id} value={indicator.id}>
                    {indicator.name}
                  </option>
                ))}
              </select>
              <small className="text-gray-500">{indicatorDescription}</small>
            </div>
          </div>

          <div className="form-control mt-4">
            <button type="submit" className="btn btn-primary bg-neutral-600" style={{ color: 'white' }}>Run Backtest</button>
          </div>
        </form>

        {results && (
          <div className="mt-6 grid grid-cols-2 gap-4">
            <div className="card p-4 bg-gray-100 rounded-lg shadow-md">
              <h3 className="text-lg font-bold">Start / End Portfolio</h3>
              <p><strong>${results.initial_cash.toFixed(2)} / ${results.final_value.toFixed(2)}</strong></p>
              <p>Total Portfolio: {results.final_value.toFixed(2)}</p>
              <p>Return Percentage: {(results.percentage_return * 100).toFixed(2)}%</p>
            </div>
            <div className="card p-4 bg-gray-100 rounded-lg shadow-md">
              <h3 className="text-lg font-bold">Win / Loss Trade</h3>
              <p><strong>{results.winning_trades} Wins / {results.losing_trades} Losses</strong></p>
              <p>Total Trade: {results.total_trades}</p>
              <p>Win Trade Percentage: {((results.winning_trades / results.total_trades) * 100).toFixed(2)}%</p>
            </div>
            <div className="card p-4 bg-gray-100 rounded-lg shadow-md">
              <h3 className="text-lg font-bold">Sharpe Ratio</h3>
              <p>{results.sharpe_ratio}</p>
            </div>
            <div className="card p-4 bg-gray-100 rounded-lg shadow-md">
              <h3 className="text-lg font-bold">Max Drawdown</h3>
              <p>{results.max_drawdown}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default BacktestForm;
