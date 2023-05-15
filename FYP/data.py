import yfinance as yf
import pandas_datareader as web

import pandas as pd
from talib import abstract
from datetime import date, timedelta




yf.pdr_override()
new_index=[]
ori=0

def calc_index(index,start,end):
    ser_index = []
    data = yf.download("^"+index, start=start, end=end)

    for ca in range(len(data['Adj Close'])):
        global ori
        if ca==0:
            ori=(data['Adj Close'][0])
        if ca==len(data['Adj Close'])-1:
            break
        ind=data['Adj Close'][ca]
        new_index.append(ind * change_of_stock(index, start, end, ca))


    new_index.insert(0,ori)

    for i in range(len(data['Adj Close'])):
        ser_index.append(data['Adj Close'].index[i])

    new = pd.Series(new_index, index=ser_index)
    old = pd.Series(data['Adj Close'])

    new.to_csv(index+'.csv',index=True)
    return new,old

def change_of_stock(index,start,end,ca):
    par = []        # parcentage change of each day of each stock
    pchange = []  #paracentage change for only 20% stock of index
    change = 1
    st=[]
    stock, parcent = get_stock_from_index(index)
    st=get_stock_data(stock,start,end)

    for x in range(len(st)):
        old = st[x]['Close'][ca]
        new = st[x]['Close'][ca+1]
        par.append((new-old)/old)

    for i in parcent:
        total = sum(parcent)
        pchange.append(i / total)

    for y in range(len(stock)):
        change = change + (par[y] * pchange[y])

    return change

def get_stock_data(stock,start,end):
    st=[] #data of the each stock
    for x in stock :
        df=(web.get_data_yahoo(x,start,end))
        st.append(df)

    return st


def get_stock_from_index(index):

    stock_switcher = {
        'HSI': ["0700.HK","1299.HK","0005.HK","0939.HK","2318.HK","0941.HK","1398.HK","0388.HK","3988.HK","0883.HK"],
        'HSCE': ['0700.HK','0939.HK','2318.HK','0941.HK','1398.HK','3988.HK','0883.HK','3968.HK','2628.HK','0386.HK'],
        'DJI': ['GS','MMM','BA','UNH','HD','IBM','MCD','AAPL','JNJ','TRV']


    }
    par_switcher={
        'HSI' : [11.54,10.82,9.75,7.4,5.53,4.46,4.43,3.53,2.75,2.36],
        'HSCE': [11.39,9.7,9.3,7.41,7.23,4.52,3.98,2.78,2.63,1.88],
        'DJI':[7.1,6.83,6.29,5.82,5.02,4.98,4.87,4.56,4.3,4.15]
    }
    return stock_switcher.get(index,""),par_switcher.get(index,"")



def technical_index(index):
    stock, parcent = get_stock_from_index(index)
    ta_list=['RSI','CCI']
    end = date.today()
    end = date.today()- timedelta(days=1)
    #datetime_object = date.strptime(end, '%Y-%m-%d')

    start = end- timedelta(days=21)

    for x in stock:
        data=web.get_data_yahoo(x,start,end)
        data.columns = ['Date', 'high', 'low', '---', 'volume', 'close']
        print(x)
        for a in ta_list:
            output=eval('abstract.'+a+'(data)')
            print(output[len(output)-1])





