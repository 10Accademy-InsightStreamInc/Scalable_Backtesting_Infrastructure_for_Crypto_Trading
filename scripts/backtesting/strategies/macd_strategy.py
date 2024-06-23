from .base_strategy import BaseStrategy
import backtrader as bt

class MACDStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        self.macd = bt.indicators.MACD(self.data.close)
        self.signal = self.macd.signal

    def buy_signal(self):
        return self.macd.macd[0] > self.signal[0]

    def sell_signal(self):
        return self.macd.macd[0] < self.signal[0]