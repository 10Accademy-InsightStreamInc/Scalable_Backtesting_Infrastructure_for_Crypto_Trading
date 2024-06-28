from .base_strategy import BaseStrategy
import backtrader as bt

class MACDStrategy(BaseStrategy):
    params = (('macd_fast', 12), ('macd_slow', 26), ('macd_signal', 9),)

    def __init__(self):
        super().__init__()
        self.macd = bt.indicators.MACD(self.data.close, 
                                       period_me1=self.params.macd_fast,
                                       period_me2=self.params.macd_slow,
                                       period_signal=self.params.macd_signal)
        self.signal = self.macd.signal

    def buy_signal(self):
        return self.macd.macd[0] > self.signal[0]

    def sell_signal(self):
        return self.macd.macd[0] < self.signal[0]