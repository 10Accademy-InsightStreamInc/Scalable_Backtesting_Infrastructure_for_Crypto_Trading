import backtrader as bt
import pandas as pd
import os
import sys

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=15)

    def next(self):
        if self.sma > self.data.close:
            self.buy()
        elif self.sma < self.data.close:
            self.sell()

if __name__ == '__main__':
    print(os.getcwd())
    cerebro = bt.Cerebro()
    df = pd.read_csv('data/binance_btc_usdt_candlestick.csv', index_col='timestamp', parse_dates=True)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(TestStrategy)
    cerebro.run()
    cerebro.plot()
