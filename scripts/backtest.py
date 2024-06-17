import backtrader as bt
import pandas as pd

class SMAStrategy(bt.Strategy):
    params = (
        ('period', 15),
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period)

    def next(self):
        if self.sma > self.data.close:
            self.buy()
        elif self.sma < self.data.close:
            self.sell()

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    df = pd.read_csv('data/binance_btc_usdt_candlestick.csv', index_col='timestamp', parse_dates=True)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    # Run backtests with different SMA periods
    for period in [10, 15, 20]:
        cerebro.addstrategy(SMAStrategy, period=period)
        print(f'Running backtest with SMA period: {period}')
        cerebro.run()
        cerebro.plot()
