import yfinance as yf
import backtrader as bt
import os, sys
import pandas as pd

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.append(project_root)

from scripts.backtesting.util.user_input import get_user_input
from scripts.backtesting.analyzers.metrics_analyzer import MetricsAnalyzer
from backend.database import get_db
from backend import models

import mlflow
import mlflow.pyfunc

def run_backtest(config):
    with mlflow.start_run():
        initial_cash = config['initial_cash']
        start_date = config['start_date']
        end_date = config['end_date']
        ticker = config['ticker']
        indicator = config['indicator']

        try:
            db = next(get_db())
            # Fetch historical data from database starting from start_date to end_date with ticker 
            stock_data = db.query(models.StockData).filter(
                models.StockData.symbol == ticker,
                models.StockData.date >= start_date,
                models.StockData.date <= end_date
            ).all()

            # Convert to list of dictionaries
            data_list = [{
                'date': data.date,
                'open': data.open,
                'high': data.high,
                'low': data.low,
                'close': data.close,
                'volume': data.volume,
                'symbol': data.symbol
            } for data in stock_data]

            # Convert to DataFrame
            data = pd.DataFrame(data_list)
            # convert date column to datetime
            data['date'] = pd.to_datetime(data['date'])
            #make the date the index
            data.set_index('date', inplace=True)
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
            from scripts.backtesting.strategies.sma_strategy import SMAStrategy
            cerebro.addstrategy(SMAStrategy)
        elif indicator == 'LSTM':
            from scripts.backtesting.strategies.lstm_strategy import run_backtest_with_lstm
            return run_backtest_with_lstm(df=data)
        elif indicator == 'MACD':
            from scripts.backtesting.strategies.macd_strategy import MACDStrategy
            cerebro.addstrategy(MACDStrategy)
        elif indicator == 'RSI':
            from scripts.backtesting.strategies.rsi_strategy import RSIStrategy
            cerebro.addstrategy(RSIStrategy)
        elif indicator == 'BB':
            from scripts.backtesting.strategies.bollinger_bands_strategy import BollingerBandsStrategy
            cerebro.addstrategy(BollingerBandsStrategy)
        else:
            print("Invalid indicator selected.")
            return

        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0, _name='sharperatio')
        cerebro.addanalyzer(MetricsAnalyzer, _name='MetricsAnalyzer')

        # Run backtest
        results = cerebro.run()
        strat = results[0]

        # Log results to MLflow
        mlflow.log_param("initial_cash", initial_cash)
        mlflow.log_param("start_date", start_date)
        mlflow.log_param("end_date", end_date)
        mlflow.log_param("ticker", ticker)
        mlflow.log_param("indicator", indicator)

        final_value = cerebro.broker.getvalue()
        sharpe_ratio = strat.analyzers.sharperatio.get_analysis()['sharperatio'] or 0
        metrics_analyzer = strat.analyzers.getbyname('MetricsAnalyzer')
        metrics = metrics_analyzer.get_analysis()
        percentage_return = metrics['return']
        total_trades = metrics['trades']
        winning_trades = metrics['winning_trades']
        losing_trades = metrics['losing_trades']

        mlflow.log_metric("final_value", final_value)
        mlflow.log_metric("sharpe_ratio", sharpe_ratio)
        mlflow.log_metric("percentage_return", percentage_return)
        mlflow.log_metric("total_trades", total_trades)
        mlflow.log_metric("winning_trades", winning_trades)
        mlflow.log_metric("losing_trades", losing_trades)

        return {
            'initial_cash': initial_cash,
            'final_value': final_value,
            'sharpe_ratio': sharpe_ratio,
            'percentage_return': percentage_return,
            'total_trades': total_trades,
            'winning_trades': winning_trades,
            'losing_trades': losing_trades
        }

if __name__ == "__main__":
    # initial_cash, start_date, end_date, ticker, indicator = get_user_input()
    config = {
        'initial_cash': 500,
        'start_date': "2024-02-01",
        'end_date': "2024-06-11",
        'ticker': "NVDA",
        'indicator': "SMA"
    }
    run_backtest(config)