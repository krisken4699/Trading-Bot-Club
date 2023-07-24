import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Bidirectional
from keras.regularizers import l2
from keras.optimizers import Adam
import matplotlib.pyplot as plt

# Replace 'AAPL' with the stock symbol you want to predict
symbol = 'ALB'

# Download historical stock price data from Yahoo Finance
df = yf.download(symbol, start='2019-01-01', end='2023-01-01')

# Feature engineering (calculate moving averages)
df['SMA_5'] = df['Close'].rolling(window=5).mean()
df['SMA_10'] = df['Close'].rolling(window=10).mean()

# Calculate Bollinger Bands
df['Upper_BB'] = df['Close'].rolling(window=20).mean() + 2 * df['Close'].rolling(window=20).std()
df['Lower_BB'] = df['Close'].rolling(window=20).mean() - 2 * df['Close'].rolling(window=20).std()

# Calculate MACD (Moving Average Convergence Divergence)
short_window = 12
long_window = 26
df['ShortEMA'] = df['Close'].ewm(span=short_window, adjust=False).mean()
df['LongEMA'] = df['Close'].ewm(span=long_window, adjust=False).mean()
df['MACD'] = df['ShortEMA'] - df['LongEMA']

# Drop rows with NaN values due to moving averages, Bollinger Bands, and MACD calculation
df.dropna(inplace=True)

# Prepare data for training
X = df[['Close', 'SMA_5', 'SMA_10', 'Upper_BB', 'Lower_BB', 'MACD', 'Volume']]
y = (df['Close'].shift(-1) > df['Close']).astype(int)

# Normalize the features using MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Reshape X to 3D array (samples, timesteps, features) for LSTM
sequence_length = 10  # Adjust sequence length as needed
X_lstm = []
y_lstm = []
for i in range(len(X_scaled) - sequence_length):
    X_lstm.append(X_scaled[i:i+sequence_length])
    y_lstm.append(y[i+sequence_length])  # Remove the -1 index to avoid IndexError

X_lstm = np.array(X_lstm)
y_lstm = np.array(y_lstm)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_lstm, y_lstm, test_size=0.2, random_state=42)

# Build the LSTM model
model = Sequential()
model.add(Bidirectional(LSTM(64, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True)))
model.add(Dropout(0.2))
model.add(Bidirectional(LSTM(32)))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid', kernel_regularizer=l2(0.001)))

# Compile the model with Adam optimizer and binary cross-entropy loss
optimizer = Adam(lr=0.001)
model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Train the LSTM model and store the training history
history = model.fit(X_train, y_train, epochs=200, batch_size=32, verbose=1, validation_split=0.1)

# Make predictions on the testing set
y_pred = (model.predict(X_test) > 0.5).astype('int').reshape(-1)

# Evaluate the LSTM model
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)

# Plot training and validation loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()