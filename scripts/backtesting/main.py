import yfinance as yf
import backtrader as bt
from util.user_input import get_user_input
from analyzers.metrics_analyzer import MetricsAnalyzer

def run_backtest(config):
    initial_cash = config['initial_cash']
    start_date = config['start_date']
    end_date = config['end_date']
    ticker = config['ticker']
    indicator = config['indicator']

    # Fetch historical data
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        data_feed = bt.feeds.PandasData(dataname=data)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # Initialize Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.adddata(data_feed)
    cerebro.broker.setcash(initial_cash)

    # Add strategy based on selected indicator
    if indicator == 'SMA':
        from strategies.sma_strategy import SMAStrategy
        cerebro.addstrategy(SMAStrategy)
    elif indicator == 'LSTM':
        from strategies.lstm_strategy import LSTMStrategy
        cerebro.addstrategy(LSTMStrategy)
    elif indicator == 'MACD':
        from strategies.macd_strategy import MACDStrategy
        cerebro.addstrategy(MACDStrategy)
    elif indicator == 'RSI':
        from strategies.rsi_strategy import RSIStrategy
        cerebro.addstrategy(RSIStrategy)
    elif indicator == 'Bollinger Bands':
        from strategies.bollinger_bands_strategy import BollingerBandsStrategy
        cerebro.addstrategy(BollingerBandsStrategy)
    else:
        print("Invalid indicator selected.")
        return

    # Add analyzers
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0, annualized=True)
    cerebro.addanalyzer(MetricsAnalyzer)

    # Run backtest
    results = cerebro.run()
    strat = results[0]

    # Print results
    print(f"Initial Cash: {initial_cash}")
    print(f"Final Value: {cerebro.broker.getvalue()}")
    print(f"Sharpe Ratio: {strat.analyzers.sharperatio.get_analysis()}")

    metrics_analyzer = strat.analyzers.getbyname('MetricsAnalyzer')
    metrics = metrics_analyzer.get_analysis()
    print(f"Return: {metrics['return']}")
    print(f"Total Trades: {metrics['trades']}")
    print(f"Winning Trades: {metrics['winning_trades']}")
    print(f"Losing Trades: {metrics['losing_trades']}")

if __name__ == "__main__":
    config = get_user_input()
    run_backtest(config)