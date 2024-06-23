from .base_strategy import BaseStrategy
import backtrader as bt

class SMAStrategy(BaseStrategy):
    params = (('sma_period', 15),)

    def __init__(self):
        super().__init__()
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_period)

    def buy_signal(self):
        return self.data.close[0] > self.sma[0]

    def sell_signal(self):
        return self.data.close[0] < self.sma[0]