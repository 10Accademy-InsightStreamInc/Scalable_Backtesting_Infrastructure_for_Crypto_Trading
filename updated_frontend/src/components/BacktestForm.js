import React, { useState } from 'react';

function BacktestForm() {
  const [parameters, setParameters] = useState({
    startDate: '',
    endDate: '',
    indicator: '',
    paramsRange: '',
  });

  const [results, setResults] = useState(null);  

  const handleChange = (e) => {
    setParameters({
      ...parameters,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(parameters);
    // Simulate API call to backend
    
    // const response = await fetch('https://localhost'); 
    const response = {
      "return": "10%",
      "numberOfTrades": 50,
      "winningTrades": 30,
      "losingTrades": 20,
      "maxDrawdown": "5%",
      "sharpeRatio": 1.5
    }
    
    // const data = await response.json();
     const data = response;
    setResults(data);
  };

  return (
    <div className="card bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">Backtest Parameters</h2>
        <form onSubmit={handleSubmit}>
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
    <option value="NVDA">NVDA</option>
    <option value="TSLA">TSLA</option>
    <option value="MC.PA">MC.PA</option>
    <option value="WMT">WMT</option>
    <option value="AMZN">AMZN</option>
  </select>
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
          <div className="form-control">
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
    <option value="SMA">SMA</option>
    <option value="LSTM">LSTM</option>
    <option value="MACD">MACD</option>
    <option value="RSI">RSI</option>
    <option value="Bollinger Bands">Bollinger Bands</option>
  </select>
</div>


          <div className="form-control mt-4">
          <button type="submit" className="btn btn-primary bg-neutral-600" style={{ color: 'white' }}>Run Backtest</button>
          </div>
        </form>

        {results && (
          <div className="mt-6">
            <h3 className="text-lg font-bold">Backtest Results</h3>
            <div className="p-4 bg-gray-100 rounded-lg">
              <p><strong>Return:</strong> {results.return}</p>
              <p><strong>Number of Trades:</strong> {results.numberOfTrades}</p>
              <p><strong>Winning Trades:</strong> {results.winningTrades}</p>
              <p><strong>Losing Trades:</strong> {results.losingTrades}</p>
              <p><strong>Max Drawdown:</strong> {results.maxDrawdown}</p>
              <p><strong>Sharpe Ratio:</strong> {results.sharpeRatio}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default BacktestForm;
