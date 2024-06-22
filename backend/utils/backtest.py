import backtrader as bt
import pandas as pd

class SMAStrategy(bt.Strategy):
    params = (
        ('period', 15),
    )

    def __init__(self):
        self.sma = bt.indicators.SMA(self.data.close, period=self.params.period)
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
        self.cerebro.metrics.append({
            'Period': self.params.period,
            'Gross Profit': trade.pnl,
            'Net Profit': trade.pnlcomm,
            'Number of Trades': len(self),
            'Winning Trades': len([t for t in self._trades if t.pnl > 0]),
            'Losing Trades': len([t for t in self._trades if t.pnl <= 0]),
            'Max Drawdown': self.broker.maxdrawdown,
            'Sharpe Ratio': self.broker.get_sharperatio()
        })

def run_backtest(scene, df):
    cerebro = bt.Cerebro()
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    if scene['indicator_name'] == 'SMA':
        cerebro.addstrategy(SMAStrategy, period=scene['period'])
    # Add more strategies as needed

    cerebro.metrics = []
    cerebro.run()

    return cerebro.metrics
