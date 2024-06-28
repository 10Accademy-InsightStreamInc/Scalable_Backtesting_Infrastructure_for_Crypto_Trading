# import backtrader as bt

# class BaseStrategy(bt.Strategy):
#     def __init__(self):
#         self.order = None

#     def next(self):
#         if self.order:
#             return

#         if not self.position:
#             if self.buy_signal():
#                 self.order = self.buy()
#         else:
#             if self.sell_signal():
#                 self.order = self.sell()

#     def notify_order(self, order):
#         if order.status in [order.Submitted, order.Accepted]:
#             return

#         if order.status in [order.Completed]:
#             if order.isbuy():
#                 self.log(f'BUY EXECUTED, {order.executed.price}')
#             elif order.issell():
#                 self.log(f'SELL EXECUTED, {order.executed.price}')

#         self.order = None

#     def notify_trade(self, trade):
#         if trade.isclosed:
#             self.log(f'TRADE PROFIT, GROSS {trade.pnl}, NET {trade.pnlcomm}')

#     def log(self, txt, dt=None):
#         dt = dt or self.datas[0].datetime.date(0)
#         print(f'{dt.isoformat()} {txt}')
import backtrader as bt
class BaseStrategy(bt.Strategy):
    def __init__(self):
        self.order = None

    def next(self):
        if self.order:
            return

        # Proportion of available cash to invest per trade
        cash = self.broker.get_cash()
        size = int(cash * 0.1 / self.data.close[0])  # Example: invest 10% of cash per trade

        if not self.position:
            if self.buy_signal():
                self.order = self.buy(size=size)
        else:
            if self.sell_signal():
                self.order = self.sell(size=self.position.size)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, {order.executed.price}, Size: {order.executed.size}')
            elif order.issell():
                self.log(f'SELL EXECUTED, {order.executed.price}, Size: {order.executed.size}')

        self.order = None

    def notify_trade(self, trade):
        if trade.isclosed:
            self.log(f'TRADE PROFIT, GROSS {trade.pnl}, NET {trade.pnlcomm}')

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')