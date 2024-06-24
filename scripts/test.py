import json
import backtrader as bt
import yfinance as yf
import os
import pandas as pd
from datetime import datetime

# Base Strategy Class
class BaseStrategy(bt.Strategy):
    def __init__(self):
        self.order = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.buy_signal():
                self.order = self.buy()
        else:
            if self.sell_signal():
                self.order = self.sell()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, {order.executed.price}')
            elif order.issell():
                self.log(f'SELL EXECUTED, {order.executed.price}')

        self.order = None

    def notify_trade(self, trade):
        if trade.isclosed:
            self.log(f'TRADE PROFIT, GROSS {trade.pnl}, NET {trade.pnlcomm}')

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')

# SMA Strategy
class SMAStrategy(BaseStrategy):
    params = (('sma_period', 15),)

    def __init__(self):
        super().__init__()
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_period)

    def buy_signal(self):
        return self.data.close[0] > self.sma[0]

    def sell_signal(self):
        return self.data.close[0] < self.sma[0]

# Placeholder for LSTM Strategy (Requires pre-trained model and more complex setup)
class LSTMStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        # Load your pre-trained LSTM model here
        # self.lstm_model = load_model('path_to_lstm_model')

    def buy_signal(self):
        # Implement LSTM prediction logic here
        return False  # Placeholder

    def sell_signal(self):
        # Implement LSTM prediction logic here
        return False  # Placeholder

# MACD Strategy
class MACDStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        self.macd = bt.indicators.MACD(self.data.close)
        self.signal = self.macd.signal

    def buy_signal(self):
        return self.macd.macd[0] > self.signal[0]

    def sell_signal(self):
        return self.macd.macd[0] < self.signal[0]

# RSI Strategy
class RSIStrategy(BaseStrategy):
    params = (('rsi_period', 14), ('rsi_overbought', 70), ('rsi_oversold', 30),)

    def __init__(self):
        super().__init__()
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data.close, period=self.params.rsi_period)

    def buy_signal(self):
        return self.rsi[0] < self.params.rsi_oversold

    def sell_signal(self):
        return self.rsi[0] > self.params.rsi_overbought

# Bollinger Bands Strategy
class BollingerBandsStrategy(BaseStrategy):
    params = (('bb_period', 20), ('bb_devfactor', 2.0),)

    def __init__(self):
        super().__init__()
        self.bb = bt.indicators.BollingerBands(self.data.close, period=self.params.bb_period, devfactor=self.params.bb_devfactor)

    def buy_signal(self):
        return self.data.close[0] < self.bb.bot[0]

    def sell_signal(self):
        return self.data.close[0] > self.bb.top[0]

# Analyzer Class
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

        

# Function to get user input
def get_user_input():
    initial_cash = float(input("Enter initial cash: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    stocks = {
        '1': 'NVDA',
        '2': 'TSLA',
        '3': 'MC.PA',
        '4': 'WMT',
        '5': 'AMZN'
    }
    
    print("Choose a stock:")
    for key, value in stocks.items():
        print(f"{key}: {value}")
    
    stock_choice = input("Enter the number corresponding to your choice: ")
    ticker = stocks.get(stock_choice, 'NVDA')

    indicators = {
        '1': 'SMA',
        '2': 'LSTM',
        '3': 'MACD',
        '4': 'RSI',
        '5': 'Bollinger Bands'
    }
    
    print("Choose an indicator:")
    for key, value in indicators.items():
        print(f"{key}: {value}")

    indicator_choice = input("Enter the number corresponding to your choice: ")
    indicator = indicators.get(indicator_choice, 'SMA')

    return initial_cash, start_date, end_date, ticker, indicator

# Function to run the backtest
def run_backtest(config):
    initial_cash = config['initial_cash']
    start_date = config['start_date']
    end_date = config['end_date']
    ticker = config['ticker']
    indicator = config['indicator']

    # Fetch historical data
    data = yf.download(ticker, start=start_date, end=end_date)
    data_feed = bt.feeds.PandasData(dataname=data)

    # Initialize Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.adddata(data_feed)
    cerebro.broker.setcash(initial_cash)
    
    # Add strategy based on selected indicator
    if indicator == 'SMA':
        cerebro.addstrategy(SMAStrategy)
    elif indicator == 'LSTM':
        cerebro.addstrategy(LSTMStrategy)
    elif indicator == 'MACD':
        cerebro.addstrategy(MACDStrategy)
    elif indicator == 'RSI':
        cerebro.addstrategy(RSIStrategy)
    elif indicator == 'Bollinger Bands':
        cerebro.addstrategy(BollingerBandsStrategy)

    # Add analyzer
    cerebro.addanalyzer(MetricsAnalyzer, _name='metrics')
    
    # Run backtest
    results = cerebro.run()
    metrics = results[0].analyzers.metrics.get_analysis()
    
    # Print final results
    print(f'Final Portfolio Value: {cerebro.broker.getvalue()}')
    print(f"Return: {metrics['return'] * 100:.2f}%")
    print(f"Number of Trades: {metrics['trades']}")
    print(f"Winning Trades: {metrics['winning_trades']}")
    print(f"Losing Trades: {metrics['losing_trades']}")

# Main function
def main():
    initial_cash, start_date, end_date, ticker, indicator = get_user_input()
    config = {
        'initial_cash': initial_cash,
        'start_date': start_date,
        'end_date': end_date,
        'ticker': ticker,
        'indicator': indicator
    }
    run_backtest(config)

if __name__ == '__main__':
    main()