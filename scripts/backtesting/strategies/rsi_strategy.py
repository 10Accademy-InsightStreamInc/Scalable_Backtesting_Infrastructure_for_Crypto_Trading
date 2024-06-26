from .base_strategy import BaseStrategy
import backtrader as bt

class RSIStrategy(BaseStrategy):
    params = (('rsi_period', 14), ('rsi_overbought', 70), ('rsi_oversold', 30),)

    def __init__(self):
        super().__init__()
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data.close, period=self.params.rsi_period)

    def buy_signal(self):
        return self.rsi[0] < self.params.rsi_oversold

    def sell_signal(self):
        return self.rsi[0] > self.params.rsi_overbought