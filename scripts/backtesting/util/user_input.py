def get_user_input():
    initial_cash = float(input("Enter initial cash: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    print("Choose a stock:")
    from .stock_selection import stocks
    for key, value in stocks.items():
        print(f"{key}: {value}")
    
    stock_choice = input("Enter the number corresponding to your choice: ")
    ticker = stocks.get(stock_choice, 'NVDA')

    print("Choose an indicator:")
    indicators = {
        '1': 'SMA',
        '2': 'LSTM',
        '3': 'MACD',
        '4': 'RSI',
        '5': 'Bollinger Bands'
    }
    for key, value in indicators.items():
        print(f"{key}: {value}")

    indicator_choice = input("Enter the number corresponding to your choice: ")
    indicator = indicators.get(indicator_choice, 'SMA')

    return initial_cash, start_date, end_date, ticker, indicator