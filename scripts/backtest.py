import backtrader as bt
import pandas as pd

class SMAStrategy(bt.Strategy):
    params = (
        ('period', 15),
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.period)
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def next(self):
        if self.order:
            return

        if self.sma > self.data.close:
            self.order = self.buy()
        elif self.sma < self.data.close:
            self.order = self.sell()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:
                self.sellprice = order.executed.price
                self.sellcomm = order.executed.comm

            self.bar_executed = len(self)

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        print(f'Operation Profit, Gross {trade.pnl}, Net {trade.pnlcomm}')

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    df = pd.read_csv('data/binance_btc_usdt_candlestick.csv', index_col='timestamp', parse_dates=True)
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    metrics = []

    for period in [10, 15, 20]:
        cerebro.addstrategy(SMAStrategy, period=period)
        print(f'Running backtest with SMA period: {period}')
       
