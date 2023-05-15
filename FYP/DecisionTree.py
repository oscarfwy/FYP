import yfinance as yf

stk = yf.Ticker('SPY')
data = stk.history(start = '2000-01-01')
print (len(data))
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]


import pandas as pd
from talib import abstract

data.columns = ['open','high','low','close','volume']
ta_list = ['MACD','RSI','MOM','STOCH','ATR','ADX']

for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')

import numpy as np


data['week_trend'] = np.where(data.close.shift(-5) > data.close, 1, 0)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

df = data['2019'].copy()
df = df.resample('D').ffill()

t = mdates.drange(df.index[0], df.index[-1], dt.timedelta(hours = 24))
y = np.array(df.close[:-1])

fig, ax = plt.subplots()
ax.plot_date(t, y, 'b-', color = 'black')
for i in range(len(df)):
    if df.week_trend[i] == 1:
        ax.axvspan(
            mdates.datestr2num(df.index[i].strftime('%Y-%m-%d')) - 0.5,
            mdates.datestr2num(df.index[i].strftime('%Y-%m-%d')) + 0.5,
            facecolor = 'red', edgecolor = 'none', alpha = 0.5
            )
    else:
        ax.axvspan(
            mdates.datestr2num(df.index[i].strftime('%Y-%m-%d')) - 0.5,
            mdates.datestr2num(df.index[i].strftime('%Y-%m-%d')) + 0.5,
            facecolor = 'green', edgecolor = 'none', alpha = 0.5
            )
fig.autofmt_xdate()
fig.set_size_inches(20, 10.5)


data.isnull().sum()
#remove nan value
data = data.dropna()

#seperate data for learn and test 70%
split_point = int(len(data)*0.9)
#cut for train and test
train = data.iloc[:split_point,:].copy()
test = data.iloc[split_point:-5,:].copy()

#train AI
train_X = train.drop('week_trend', axis = 1)
train_y = train.week_trend
#test AI
test_X = test.drop('week_trend', axis = 1)
test_y = test.week_trend


from sklearn.tree import DecisionTreeClassifier

#call decision tree
model = DecisionTreeClassifier(max_depth = 10)

#let AI train
model.fit(train_X, train_y)

#let AI test and save the answer
prediction = model.predict(test_X)



#print (prediction)
if prediction[len(prediction)-1] ==0:
    print('It predict the price will decrease')
else:
    print('It predict the price will increase')



from sklearn.metrics import confusion_matrix

#find the result accuracy
print(confusion_matrix(test_y, prediction))

#accuracy
print(model.score(test_X, test_y))



#data.to_csv('file.csv',index=True)

