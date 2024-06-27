from tensorflow.keras.models import load_model
import joblib
import numpy as np
import os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.append(project_root)
print("Before loading", os.getcwd())
def load_lstm_model_and_scaler(model_path='my_model.keras', scaler_path='scaler.gz'):
    print("After loading", os.getcwd())
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

def run_backtest_with_lstm(df):
    lstm_model, scaler = load_lstm_model_and_scaler()
    predictions = make_lstm_predictions(lstm_model, scaler, df)
    
    initial_cash = 10000
    cash = initial_cash
    position = 0  # 1 for holding stock, 0 for no stock
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
    
    # Calculate metrics
    final_value = cash + position * df['Close'].values[-1]
    gross_profit = final_value - initial_cash
    metrics = {
        'initial_cash': initial_cash,
        'final_value': final_value,  # Add any transaction costs if applicable
        'number_of_trades': position,
        'winning_trades': position if gross_profit > 0 else 0,
        'losing_trades': position if gross_profit <= 0 else 0,
        'max_drawdown': -1000,  # Calculate this properly based on your strategy
        'sharpe_ratio': 1.5     # Calculate this properly based on your strategy
    }
    return metrics