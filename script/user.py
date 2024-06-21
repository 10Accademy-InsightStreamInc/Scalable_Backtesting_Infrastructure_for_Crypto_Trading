import backtrader as bt
import yfinance as yf
from datetime import datetime

def get_user_input():
    initial_cash = float(input("Enter initial cash: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    return initial_cash, start_date, end_date

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

def run_backtest(initial_cash, start_date, end_date):
    # Download NVDA stock data from Yahoo Finance
    df = yf.download('NVDA', start=start_date, end=end_date)

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
    print(f"Return: {metrics['return']:.2f}")
    print(f"Number of trades: {metrics['trades']}")
    print(f"Winning trades: {metrics['winning_trades']}")
    print(f"Losing trades: {metrics['losing_trades']}")
    print(f"Max drawdown: {strat.analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")

    sharpe_ratio = strat.analyzers.sharpe.get_analysis().get('sharperatio', None)
    if sharpe_ratio is not None:
        print(f"Sharpe ratio: {sharpe_ratio:.2f}")
    else:
        print("Sharpe ratio: N/A")

    # Plot the results
    cerebro.plot()

if __name__ == '__main__':
    initial_cash, start_date, end_date = get_user_input()
    run_backtest(initial_cash, start_date, end_date)