from flask import Flask, render_template, request, redirect
import yfinance as yf
import numpy as np
import pandas as pd
import pickle


from sklearn.linear_model import LinearRegression


model=pickle.load(open('model.pkl','rb'))
#pickle.dump(main(),open('model.pkl','wb'))
app = Flask(__name__)
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

def main(stock_ticker,future_date_str):
    # Get the stock ticker from the user
    #stock_ticker = input("Enter the stock ticker (e.g., AAPL): ")

    # Train the stock prediction model
    stock_model = train_stock_prediction_model(stock_ticker)

    # Get the future date from the user
   # future_date_str = input("Enter the future date in YYYY-MM-DD format: ")
    future_date = pd.to_datetime(future_date_str)

    # Predict the future stock price
    predicted_price = 1.25*predict_future_stock_price(stock_model, future_date)

    #return(f'Predicted Stock Price on {future_date}: ${predicted_price:.2f}')
    return predicted_price
    



from datetime import datetime





    
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')
@app.route('/stocks', methods=['GET', 'POST'])
def hello():
    return render_template('page1.html')
@app.route('/prediction', methods=['GET', 'POST'])
def world():
    return render_template('ind.html')



@app.route('/predict',methods=['POST','GET'])
def predict():
    
    date=request.form['date']
    name=request.form["name"]
    #int_features=[x for x in request.form.values()]
    #final=[np.array(int_features)]
    #print(int_features)
    #print(final)
    prediction=main(name, pd.to_datetime(date))
    return "                                   \t"+str(prediction)
    #n render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")





if __name__ == "__main__":
    app.run(debug=True, port=8000)