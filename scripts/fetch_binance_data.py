import requests
import pandas as pd
import os

def fetch_candlestick_data(symbol, interval, start, end, api_key):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start}&endTime={end}"
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 
        'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 
        'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

if __name__ == '__main__':
    API_KEY = os.getenv('BINANCE_API_KEY')
    symbol = 'BTCUSDT'
    interval = '1d'
    start = 1622505600000  # Start timestamp in milliseconds
    end = 1625097600000    # End timestamp in milliseconds
    df = fetch_candlestick_data(symbol, interval, start, end, API_KEY)
    df.to_csv(f'btc_usdt_candlestick_{start}_to_{end}.csv')
    print(df.head())
