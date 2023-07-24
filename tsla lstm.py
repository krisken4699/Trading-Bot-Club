import numpy as np
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import pandas as pd
import requests
import json
import yfinance as yf
import pytz

# import datetime
from datetime import date, timedelta, datetime
# i am sorry to have pasted it here

data2 = yf.download('TSLA',
                   interval="1d",
                   period="1y",
                   auto_adjust=True,
                   ignore_tz=True,
                   progress=False)
# print(requests.get('https://query2.finance.yahoo.com/v8/finance/chart/TSLA?range=1y&interval=1d', verify=False).status_code)
# data2 = response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
data2["Date"] = data2.index
data2 = data2[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data2.reset_index(drop=True, inplace=True)
data2.tail()
print(data2)

figure = go.Figure(data=[go.Candlestick(x=data2["Date"],
                                        open=data2["Open"],
                                        high=data2["High"],
                                        low=data2["Low"],
                                        close=data2["Close"])])
figure.update_layout(title="Tesla Stock Price Analysis",
                     xaxis_rangeslider_visible=False)
figure.show()
correlation = data2.corr()
print(correlation["Close"].sort_values(ascending=False))
x = data2[["Open", "High", "Low", "Volume"]]
y = data2["Close"]
x = x.to_numpy()
y = y.to_numpy()
y = y.reshape(-1, 1)

xtrain, xtest, ytrain, ytest = train_test_split(
    x, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(xtrain.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.summary()

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(xtrain, ytrain, batch_size=1, epochs=30)

# features = [Open, High, Low, Adj Close, Volume]
features = np.array([[177.089996, 180.419998, 177.070007, 74919600]])
# print("Open: %s High: %s Low: %s Volume: %s" % (features[0], features[1], features[2], features[3] ))
print("Prediction:",model.predict(features))