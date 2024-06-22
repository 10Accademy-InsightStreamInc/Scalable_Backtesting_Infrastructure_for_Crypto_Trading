import requests
import json

# URL of the API endpoint
url = "http://127.0.0.1:8000/indicators/"

# List of strategy indicators
indicators = [
  {
    "name": "Simple Moving Average",
    "symbol": "SMA",
    "description": "A simple, widely-used indicator that calculates the average of a selected range of prices, typically closing prices, by the number of periods in that range."
  },
  {
    "name": "LSTM",
    "symbol": "LSTM",
    "description": "A type of recurrent neural network capable of learning long-term dependencies. Used for time-series forecasting due to its ability to remember information over long periods."
  },
  {
    "name": "Moving Average Convergence Divergence",
    "symbol": "MACD",
    "description": "A trend-following momentum indicator that shows the relationship between two moving averages of a security’s price. It includes a MACD line, a signal line, and a histogram."
  },
  {
    "name": "Relative Strength Index",
    "symbol": "RSI",
    "description": "A momentum oscillator that measures the speed and change of price movements. RSI oscillates between zero and 100, typically used to identify overbought or oversold conditions."
  },
  {
    "name": "Bollinger Bands",
    "symbol": "BB",
    "description": "A volatility indicator that consists of a middle band (SMA) and two outer bands set two standard deviations away from the middle band. Used to identify overbought and oversold conditions."
  }
]

# Headers for the POST request
headers = {
    "Content-Type": "application/json"
}

# Iterate over the list of indicators and send POST requests
for indicator in indicators:
    response = requests.post(url, data=json.dumps(indicator), headers=headers)
    if response.status_code == 200:
        print(f"Successfully added {indicator['name']}")
    else:
        print(f"Failed to add {indicator['name']}: {response.status_code} - {response.text}")
