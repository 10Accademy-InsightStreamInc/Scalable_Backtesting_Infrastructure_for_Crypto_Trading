import json
import backtrader as bt
import yfinance as yf
import os
import pandas as pd
from datetime import datetime

class SMAStrategy(bt.Strategy):
    params = (('sma_period', 15),)

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.sma_period)
        self.order = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.data.close[0] > self.sma[0]:
                self.order = self.buy()
        else:
            if self.data.close[0] < self.sma[0]:
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

def get_user_input():
    initial_cash = float(input("Enter initial cash: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    return initial_cash, start_date, end_date

def generate_unique_key(ticker, start_date, end_date):
    return f"{ticker}_{start_date}_{end_date}"

def save_results_to_csv(results, csv_file):
    df = pd.DataFrame([results])
    if not os.path.isfile(csv_file):
        df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, mode='a', header=False, index=False)

def load_results_from_csv(key, csv_file):
    if os.path.isfile(csv_file):
        df = pd.read_csv(csv_file)
        result = df[df['key'] == key]
        if not result.empty:
            return result.to_dict('records')[0]
    return None

def run_backtest(config):
    initial_cash = config['initial_cash']
    start_date = config['start_date']
    end_date = config['end_date']
    ticker = config['ticker']

    # Generate unique key
    key = generate_unique_key(ticker, start_date, end_date)

    # Check if results already exist
    csv_file = 'backtest_results.csv'
    existing_result = load_results_from_csv(key, csv_file)
    if existing_result:
        print("Results already exist. Loading from file.")
        print(json.dumps(existing_result, indent=4))
        return

    # Download stock data from Yahoo Finance
    df = yf.download(ticker, start=start_date, end=end_date)

    # Create a Cerebro instance
    cerebro = bt.Cerebro()

    # Add the strategy
    cerebro.addstrategy(SMAStrategy)

    # Convert the DataFrame to Backtrader format and add it to Cerebro
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)

    # Set initial cash
    cerebro.broker.set_cash(initial_cash)

    # Add analyzers for metrics
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(MetricsAnalyzer, _name='metrics')

    # Run the backtest
    results = cerebro.run()
    strat = results[0]

    # Extract metrics
    metrics = strat.analyzers.metrics.get_analysis()
    sharpe_ratio = strat.analyzers.sharpe.get_analysis().get('sharperatio', None)
    drawdown = strat.analyzers.drawdown.get_analysis()['max']['drawdown']

    # Prepare results
    backtest_results = {
        "key": key,
        "ticker": ticker,
        "initial_cash": initial_cash,
        "start_date": start_date,
        "end_date": end_date,
        "metrics": {
            "return": metrics['return'],
            "number_of_trades": metrics['trades'],
            "winning_trades": metrics['winning_trades'],
            "losing_trades": metrics['losing_trades'],
            "max_drawdown": drawdown,
            "sharpe_ratio": sharpe_ratio if sharpe_ratio is not None else "N/A"
        }
    }

    # Save the results to CSV
    save_results_to_csv(backtest_results, csv_file)

    # Print results
    print(json.dumps(backtest_results, indent=4))

if __name__ == '__main__':
    with open('config.json', 'r') as f:
        config = json.load(f)

    initial_cash, start_date, end_date = get_user_input()
    config['initial_cash'] = initial_cash
    config['start_date'] = start_date
    config['end_date'] = end_date

    run_backtest(config)