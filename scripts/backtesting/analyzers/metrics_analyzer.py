import backtrader as bt

class MetricsAnalyzer(bt.Analyzer):
    def __init__(self):
        self.init_cash = self.strategy.broker.get_cash()
        self.end_cash = self.init_cash
        self.trades = []

    def notify_cashvalue(self, cash, value):
        self.end_cash = cash

    def notify_trade(self, trade):
        if trade.isclosed:
            self.trades.append(trade)

    def get_analysis(self):
        return {
            'return': (self.end_cash - self.init_cash) / self.init_cash,
            'trades': len(self.trades),
            'winning_trades': len([trade for trade in self.trades if trade.pnl > 0]),
            'losing_trades': len([trade for trade in self.trades if trade.pnl <= 0])
        }