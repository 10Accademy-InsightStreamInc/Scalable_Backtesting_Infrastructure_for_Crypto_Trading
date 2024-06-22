import streamlit as st
from indicators import run_backtest

st.title("Backtest App")

# Create input fields for user input
initial_cash = st.number_input("Initial Cash")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# List of available tickers
tickers = ['NVDA', 'TSLA', 'MC.PA', 'WMT', 'AMZN']

# Create a dropdown menu for the ticker
ticker = st.selectbox("Ticker", tickers)

# Create a dropdown menu for the indicator
indicators = ['SMA', 'LSTM', 'MACD', 'RSI', 'Bollinger Bands']
indicator = st.selectbox("Indicator", indicators)

# Create a dictionary to store the input values
inputs = {
    "initial_cash": initial_cash,
    "start_date": start_date,
    "end_date": end_date,
    "ticker": ticker,
    "indicator": indicator
}

# Create a button to trigger the backtest
if st.button("Run Backtest"):
    results = run_backtest({
        "initial_cash": initial_cash,
        "start_date": start_date,
        "end_date": end_date,
        "ticker": ticker,
        "indicator": indicator
    })

    # Display the results
    st.header("Backtest Results")
    st.write(f"Return: {(results['metrics']['return']):.2%}")
    st.write(f"Number of Trades: {results['metrics']['number_of_trades']}")
    st.write(f"Winning Trades: {results['metrics']['winning_trades']}")
    st.write(f"Losing Trades: {results['metrics']['losing_trades']}")
    st.write(f"Max Drawdown: {results['metrics']['max_drawdown']:.2%}")
    st.write(f"Sharpe Ratio: {results['metrics']['sharpe_ratio']}")
    