import requests
import json

# URL of the API endpoint
url = "http://127.0.0.1:8000/stocks/"

# List of companies
companies = [
    {
        "name": "Apple Inc",
        "symbol": "AAPL",
        "description": "Apple is a trillion-dollar company"
    },
    {
        "name": "Microsoft Corporation",
        "symbol": "MSFT",
        "description": "Microsoft is a multinational technology company"
    },
    {
        "name": "Amazon.com Inc",
        "symbol": "AMZN",
        "description": "Amazon is a multinational technology company focusing on e-commerce, cloud computing, and AI"
    },
    {
        "name": "Alphabet Inc",
        "symbol": "GOOGL",
        "description": "Alphabet is the parent company of Google"
    },
    {
        "name": "Facebook, Inc.",
        "symbol": "FB",
        "description": "Facebook is a social media and technology company"
    },
    {
        "name": "Berkshire Hathaway Inc",
        "symbol": "BRK.A",
        "description": "Berkshire Hathaway is a multinational conglomerate holding company"
    },
    {
        "name": "Tesla Inc",
        "symbol": "TSLA",
        "description": "Tesla is an electric vehicle and clean energy company"
    },
    {
        "name": "Alibaba Group Holding Limited",
        "symbol": "BABA",
        "description": "Alibaba is a multinational conglomerate specializing in e-commerce, retail, Internet, and technology"
    },
    {
        "name": "Tencent Holdings Limited",
        "symbol": "TCEHY",
        "description": "Tencent is a multinational conglomerate holding company"
    },
    {
        "name": "Johnson & Johnson",
        "symbol": "JNJ",
        "description": "Johnson & Johnson is a multinational corporation focusing on medical devices, pharmaceuticals, and consumer goods"
    },
    {
        "name": "Visa Inc",
        "symbol": "V",
        "description": "Visa is a multinational financial services corporation"
    },
    {
        "name": "Walmart Inc",
        "symbol": "WMT",
        "description": "Walmart is a multinational retail corporation operating a chain of hypermarkets"
    },
    {
        "name": "NVIDIA Corporation",
        "symbol": "NVDA",
        "description": "NVIDIA is a multinational technology company specializing in graphics processing units and AI"
    },
    {
        "name": "Samsung Electronics Co Ltd",
        "symbol": "SSNLF",
        "description": "Samsung is a multinational conglomerate"
    },
    {
        "name": "Procter & Gamble Co",
        "symbol": "PG",
        "description": "Procter & Gamble is a multinational consumer goods corporation"
    }
]

# Headers for the POST request
headers = {
    "Content-Type": "application/json"
}

# Iterate over the list of companies and send POST requests
for company in companies:
    response = requests.post(url, data=json.dumps(company), headers=headers)
    if response.status_code == 200:
        print(f"Successfully added {company['name']}")
    else:
        print(f"Failed to add {company['name']}: {response.status_code} - {response.text}")
