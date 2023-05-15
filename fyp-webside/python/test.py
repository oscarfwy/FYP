import yfinance as yf

stk = yf.Ticker('SPY')
# 取得 2000 年至今的資料
data = stk.history(start = '2000-01-01')
# 簡化資料，只取開、高、低、收以及成交量
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

import pandas as pd
from talib import abstract

# 改成 TA-Lib 可以辨識的欄位名稱
data.columns = ['open','high','low','close','volume']
# 隨意試試看這幾個因子好了
ta_list = ['MACD','RSI','MOM','STOCH']
# 快速計算與整理因子
for x in ta_list:
    output = eval('abstract.'+x+'(data)')
    output.name = x.lower() if type(output) == pd.core.series.Series else None
    data = pd.merge(data, pd.DataFrame(output), left_on = data.index, right_on = output.index)
    data = data.set_index('key_0')

import numpy as np

# 五日後漲標記 1，反之標記 0
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
# 最簡單的作法是把有缺值的資料整列拿掉
data = data.dropna()

# 決定切割比例為 70%:30%
split_point = int(len(data)*0.7)
# 切割成學習樣本以及測試樣本
train = data.iloc[:split_point,:].copy()
test = data.iloc[split_point:-5,:].copy()

# 訓練樣本再分成目標序列 y 以及因子矩陣 X
train_X = train.drop('week_trend', axis = 1)
train_y = train.week_trend
# 測試樣本再分成目標序列 y 以及因子矩陣 X
test_X = test.drop('week_trend', axis = 1)
test_y = test.week_trend

# 匯入決策樹分類器
from sklearn.tree import DecisionTreeClassifier

# 叫出一棵決策樹
model = DecisionTreeClassifier(max_depth = 7)

# 讓 A.I. 學習
model.fit(train_X, train_y)

# 讓 A.I. 測驗，prediction 存放了 A.I. 根據測試集做出的預測
prediction = model.predict(test_X)

print(prediction)


# 要計算混淆矩陣的話，要從 metrics 裡匯入 confusion_matrix
from sklearn.metrics import confusion_matrix

# 混淆矩陣
print(confusion_matrix(test_y, prediction))

# 準確率
print(model.score(test_X, test_y))



#data.to_csv('file.csv',index=True)

