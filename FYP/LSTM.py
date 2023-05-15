# importing required libraries
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# creating dataframe

stk = yf.Ticker('DJI')
df = stk.history(start = '2000-01-01')


new_data = pd.DataFrame(index=range(0, len(df)), columns=['Date', 'Close'])

for i in range(0, len(df)):
    new_data['Date'][i] = df.index[i]
    new_data['Close'][i] = df['Close'][i]





# setting index

new_data.index = new_data.Date

new_data.drop('Date', axis=1, inplace=True)


# creating train and test sets

dataset = new_data.values



train = dataset[0:3699, :]

valid = dataset[3699:, :]

# converting dataset into x_train and y_train

scaler = MinMaxScaler(feature_range=(0, 1))

scaled_data = scaler.fit_transform(dataset)

x_train, y_train = [], []

for i in range(len(train)):
    x_train.append(scaled_data[i])

    y_train.append(scaled_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# create and fit the LSTM network

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))

model.add(LSTM(units=50))

model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)



#DATA
inputs = new_data.values

inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)



X_test = []

for i in range(inputs.shape[0]):
    X_test.append(inputs[i])

X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

inputs=np.reshape(inputs,(inputs.shape[0],inputs.shape[1],1))


closing_price = model.predict(inputs)

print(closing_price)
closing_price = scaler.inverse_transform(closing_price)
print(closing_price)

#print(closing_price[len(closing_price)-1])
#print(closing_price)

