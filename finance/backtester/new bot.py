import alpaca_trade_api as tradeapi
# import tuliply as ti
import pandas as pd
import time

# Define API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'

# Define trading parameters
symbol = 'AAPL'
timeframe = '15Min'
rsi_length = 14
macd_fast = 12
macd_slow = 26
macd_signal = 9
ma_length = 50

# Connect to Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL)

# Define function to retrieve historical data
def get_historical_data(symbol, timeframe):
    historical_data = api.get_bars(symbol, timeframe, limit=200).df[symbol]
    return historical_data

# Define function to calculate RSI indicator
def calculate_rsi(data, rsi_length):
    rsi_values = pd.rsi(data['close'], rsi_length)
    return rsi_values

# Define function to calculate MACD and MACD-LazyBear indicators
def calculate_macd(data, macd_fast, macd_slow, macd_signal):
    macd, macd_signal, macd_hist = pd.macd(data['close'], macd_fast, macd_slow, macd_signal)
    macd_lazybear = pd.sma(macd_hist, 9)
    return macd, macd_signal, macd_hist, macd_lazybear

# Define function to calculate moving average indicator
def calculate_ma(data, ma_length):
    ma_values = pd.sma(data['close'], ma_length)
    return ma_values

# Define function to check if a buy/sell signal should be triggered
def check_signals(data, macd_signal=None):
    rsi_values = calculate_rsi(data, rsi_length)
    macd, macd_signal, macd_hist, macd_lazybear = calculate_macd(data, macd_fast, macd_slow, macd_signal)
    ma_values = calculate_ma(data, ma_length)
    last_rsi = rsi_values[-1]
    last_macd = macd[-1]
    last_macd_signal = macd_signal[-1]
    last_macd_lazybear = macd_lazybear[-1]
    last_ma = ma_values[-1]
    prev_macd = macd[-2]
    prev_macd_signal = macd_signal[-2]
    prev_macd_lazybear = macd_lazybear[-2]
    prev_ma = ma_values[-2]
    if last_rsi < 30 and last_macd > last_macd_signal and prev_macd < prev_macd_signal and last_macd_lazybear > prev_macd_lazybear and last_ma > prev_ma:
        return 'buy'
    elif last_rsi > 70 or last_macd < last_macd_signal:
        return 'sell'
    else:
        return 'hold'

# Define function to execute a trade
def execute_trade(action):
    if action == 'buy':
        api.submit_order(
            symbol=symbol,
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif action == 'sell':
        api.submit_order(
            symbol=symbol,
            qty=1,
            side='sell',
            type='market',
            time_in_force='gtc'
        )

# Run trading bot
while True:
    historical_data = get_historical_data(symbol, timeframe)
    signal = check_signals(historical_data)
    execute_trade(signal)
    time.sleep(60)
