import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import yfinance as yf
import matplotlib.pyplot as plt

def train_stock_prediction_model(ticker):
    # Download historical stock data from Yahoo Finance
    stock_data = yf.download(ticker, start='2020-01-01', end='2022-01-01')

    # Feature engineering: Extract day of year
    stock_data['DayOfYear'] = stock_data.index.dayofyear

    # Create features (X) and target variable (y)
    X = stock_data[['DayOfYear']]
    y = stock_data['Close']

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return model, stock_data

def predict_future_stock_price(model, input_date):
    # Extract day of year from the input date
    day_of_year = input_date.timetuple().tm_yday

    # Predict the future stock price
    future_price = model.predict([[day_of_year]])

    return future_price[0]

def plot_stock_data(stock_data, predicted_date, predicted_price):
    plt.figure(figsize=(10, 6))

    # Plot historical stock data
    plt.plot(stock_data.index, stock_data['Close'], label='Historical Stock Price', color='blue')

    # Highlight the predicted future stock price
    plt.scatter(predicted_date, predicted_price, color='red', label='Predicted Price')

    plt.title(f'Stock Price Prediction for {stock_data.index[-1].date()}')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Get the stock ticker from the user
    stock_ticker = input("Enter the stock ticker (e.g., AAPL): ")

    # Train the stock prediction model and get historical data
    stock_model, historical_data = train_stock_prediction_model(stock_ticker)

    # Get the future date from the user
    future_date_str = input("Enter the future date in YYYY-MM-DD format: ")
    future_date = pd.to_datetime(future_date_str)

    # Predict the future stock price
    predicted_price = predict_future_stock_price(stock_model, future_date)

    # Plot historical stock data and predicted future stock price
    plot_stock_data(historical_data, future_date, predicted_price)

    print(f'Predicted Stock Price on {future_date}: ${predicted_price:.2f}')

if __name__ == "__main__":
    main()