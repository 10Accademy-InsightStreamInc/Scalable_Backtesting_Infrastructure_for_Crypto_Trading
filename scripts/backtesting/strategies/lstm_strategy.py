from tensorflow.keras.models import load_model
import joblib
import numpy as np
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.append(project_root)
    
def load_lstm_model_and_scaler(model_path='my_model.keras', scaler_path='scaler.gz'):
    model = load_model(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

def make_lstm_predictions(model, scaler, df, seq_length=60):
    data = df['Close'].values.reshape(-1, 1)
    scaled_data = scaler.transform(data)
    X_test = []
    for i in range(seq_length, len(scaled_data)):
        X_test.append(scaled_data[i-seq_length:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    return predictions

def calculate_max_drawdown(portfolio_values):
    # Calculate drawdown
    peak = portfolio_values[0]
    max_drawdown = 0
    for value in portfolio_values:
        if value > peak:
            peak = value
        drawdown = (peak - value) / peak
        if drawdown > max_drawdown:
            max_drawdown = drawdown
    return max_drawdown

import numpy as np

def calculate_sharpe_ratio(returns, risk_free_rate=0):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

def run_backtest_with_lstm(scene_parameters, df):
    lstm_model, scaler = load_lstm_model_and_scaler()
    predictions = make_lstm_predictions(lstm_model, scaler, df)
    
    initial_cash = 10000
    cash = initial_cash
    position = 0  # 1 for holding stock, 0 for no stock
    portfolio_values = [cash]
    for i in range(len(predictions)):
        predicted_price = predictions[i]
        actual_price = df['Close'].values[-len(predictions) + i]
        
        if predicted_price > actual_price and cash > actual_price:
            # Buy signal
            cash -= actual_price
            position += 1
        elif predicted_price < actual_price and position > 0:
            # Sell signal
            cash += actual_price
            position -= 1
        portfolio_values.append(cash + position * df['Close'].values[-1])
    
    # Calculate metrics
    final_value = cash + position * df['Close'].values[-1]
    gross_profit = final_value - initial_cash
    returns = np.diff(portfolio_values) / portfolio_values[:-1]
    sharpe_ratio = calculate_sharpe_ratio(returns)
    max_drawdown = calculate_max_drawdown(portfolio_values)
    metrics = {
        'initial_cash': initial_cash,
        'final_value': final_value,  # Add any transaction costs if applicable
        'total_trades': len(predictions),  # Example, adjust as needed
        'winning_trades': sum(1 for r in returns if r > 0),
        'losing_trades': sum(1 for r in returns if r <= 0),
        'percentage_return': returns,
        'max_drawdown': max_drawdown,
        'sharpe_ratio': sharpe_ratio
    }
    return metrics