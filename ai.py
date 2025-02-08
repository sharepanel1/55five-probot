import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data
data = pd.read_csv('data/historical.csv')
numbers = data['result'].str.split(',', expand=True).astype(int)

# Normalisasi
data_normalized = numbers.values / 10.0

# Prepare LSTM sequences
X, y = [], []
for i in range(len(data_normalized)-10):
    X.append(data_normalized[i:i+10])
    y.append(data_normalized[i+10])
X = np.array(X).reshape(-1, 10, 5)
y = np.array(y)

# Bangun model
model = Sequential([
    LSTM(256, return_sequences=True, input_shape=(10, 5)),
    LSTM(128),
    Dense(5, activation='softmax')  # Output 5 angka
])
model.compile(loss='mse', optimizer='adam')
model.fit(X, y, epochs=1000, batch_size=32)
model.save('ai/model.h5')
