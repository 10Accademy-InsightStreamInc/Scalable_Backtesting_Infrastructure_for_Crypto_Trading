from .base_strategy import BaseStrategy
import backtrader as bt

class BollingerBandsStrategy(BaseStrategy):
    params = (('bb_period', 20), ('bb_devfactor', 2.0),)

    def __init__(self):
        super().__init__()
        self.bb = bt.indicators.BollingerBands(self.data.close, period=self.params.bb_period, devfactor=self.params.bb_devfactor)

    def buy_signal(self):
        return self.data.close[0] < self.bb.bot[0]

    def sell_signal(self):
        return self.data.close[0] > self.bb.top[0]