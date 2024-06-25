# test_api.py

import requests

url = "http://localhost:8000/backtest"
payload = {
    "initial_cash": 20000,
    "start_date": "2022-01-01",
    "end_date": "2024-02-11",
    "ticker": "NVDA",
    "indicator": "SMA"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())