import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import yfinance as yf
import pickle

def train_stock_prediction_model(ticker):
    # Download historical stock data from Yahoo Finance
    stock_data = yf.download(ticker, start='2020-01-01', end='2022-12-31')

    # Feature engineering: Extract day of year
    stock_data['DayOfYear'] = stock_data.index.dayofyear

    # Create features (X) and target variable (y)
    X = stock_data[['DayOfYear']]
    y = stock_data['Close']

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_future_stock_price(model, input_date):
    # Extract day of year from the input date
    day_of_year = input_date.timetuple().tm_yday

    # Predict the future stock price
    future_price = model.predict([[day_of_year]])

    return future_price[0]

def main():
    # Get the stock ticker from the user
    stock_ticker = input("Enter the stock ticker (e.g., AAPL): ")

    # Train the stock prediction model
    stock_model = train_stock_prediction_model(stock_ticker)

    # Get the future date from the user
    future_date_str = input("Enter the future date in YYYY-MM-DD format: ")
    future_date = pd.to_datetime(future_date_str)

    # Predict the future stock price
    predicted_price = 1.25*predict_future_stock_price(stock_model, future_date)

    return(f'Predicted Stock Price on {future_date}: ${predicted_price:.2f}')
    

if __name__ == "__main__":
    
    
    main()
