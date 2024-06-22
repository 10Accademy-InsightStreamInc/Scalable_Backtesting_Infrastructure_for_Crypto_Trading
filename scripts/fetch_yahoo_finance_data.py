import yfinance as yf
import pandas as pd

def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f"data/{ticker}.csv")

if __name__ == "__main__":
    start_date = "2020-01-01"
    end_date = "2021-01-01"
    download_data(f"yfinance_btc_usdt_{start_date}_to_{end_date}", start_date=start_date, end_date=end_date)
