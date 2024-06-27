# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime, timedelta
# import pandas as pd
# import yfinance as yf
# import numpy as np
# from tensorflow.keras.models import load_model
# import joblib

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 1, 1),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# dag = DAG(
#     'backtesting_dag',
#     default_args=default_args,
#     description='A simple backtesting DAG',
#     schedule_interval=timedelta(days=1),
# )

# def fetch_data(ticker="TSLA", start_date="2020-01-01", end_date=datetime.today().strftime("%Y-%m-%d")):
#     data: pd.DataFrame = yf.download(ticker, start=start_date, end=end_date)
#     data.to_csv(f'/tmp/{ticker}_{start_date}_{end_date}.csv')

# def load_lstm_model_and_scaler():
#     model = load_model('lstm_model.h5')
#     scaler = joblib.load('scaler.gz')
#     return model, scaler

# def make_lstm_predictions():
#     model, scaler = load_lstm_model_and_scaler()
#     df = pd.read_csv('/tmp/data.csv', index_col='Date', parse_dates=True)
#     data = df['Close'].values.reshape(-1, 1)
#     scaled_data = scaler.transform(data)
    
#     seq_length = 60
#     X_test = []
#     for i in range(seq_length, len(scaled_data)):
#         X_test.append(scaled_data[i-seq_length:i, 0])
    
#     X_test = np.array(X_test)
#     X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
#     predictions = model.predict(X_test)
#     predictions = scaler.inverse_transform(predictions)
#     np.save('/tmp/predictions.npy', predictions)

# def calculate_metrics():
#     df = pd.read_csv('/tmp/data.csv', index_col='Date', parse_dates=True)
#     predictions = np.load('/tmp/predictions.npy')
    
#     initial_cash = 10000
#     cash = initial_cash
#     position = 0
#     portfolio_values = [cash]
    
#     for i in range(len(predictions)):
#         predicted_price = predictions[i]
#         actual_price = df['Close'].values[-len(predictions) + i]
        
#         if predicted_price > actual_price and cash > actual_price:
#             cash -= actual_price
#             position += 1
#         elif predicted_price < actual_price and position > 0:
#             cash += actual_price
#             position -= 1
        
#         portfolio_values.append(cash + position * df['Close'].values[-1])
    
#     final_value = cash + position * df['Close'].values[-1]
#     gross_profit = final_value - initial_cash
#     overall_percentage_return = (final_value - initial_cash) / initial_cash * 100
#     returns = np.diff(portfolio_values) / portfolio_values[:-1]
#     sharpe_ratio = np.mean(returns) / np.std(returns) * np.sqrt(252)
#     max_drawdown = np.max(np.maximum.accumulate(portfolio_values) - portfolio_values) / np.maximum.accumulate(portfolio_values)
    
#     metrics = {
#         'gross_profit': gross_profit,
#         'net_profit': gross_profit,
#         'percentage_return': overall_percentage_return,
#         'sharpe_ratio': sharpe_ratio,
#         'max_drawdown': max_drawdown,
#     }
    
#     print(metrics)

# fetch_data_task = PythonOperator(
#     task_id='fetch_data',
#     python_callable=fetch_data,
#     op_args=['AAPL', '2023-01-01', '2023-12-31'],
#     dag=dag,
# )

# make_predictions_task = PythonOperator(
#     task_id='make_predictions',
#     python_callable=make_lstm_predictions,
#     dag=dag,
# )

# calculate_metrics_task = PythonOperator(
#     task_id='calculate_metrics',
#     python_callable=calculate_metrics,
#     dag=dag,
# )

# fetch_data_task >> make_predictions_task >> calculate_metrics_task
