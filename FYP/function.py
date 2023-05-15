import pandas_datareader as web
from datetime import date, timedelta
from talib import abstract

start="2000-01-01"
end=date.today()-timedelta(days=1)

def get_stock(stock):
    df = (web.get_data_yahoo(stock, start, end))
    return(df)

def technical_index(stock):
    ta_list=['RSI','MOM','CCI']
    var = []
    end = date.today()
    start = "2020-01-01"
    #end = date.today()- timedelta(days=1)
    #datetime_object = date.strptime(end, '%Y-%m-%d')

    #start = end- timedelta(days=21)

    data=web.get_data_yahoo(stock,start,end)
    data.columns = ['Date', 'high', 'low', '---', 'volume', 'close']

    for a in ta_list:
        output=eval('abstract.'+a+'(data)')
        var.append(output[len(output)-1])
        #print(output[len(output)-1])
    macd=abstract.MACD(data)
    var.append(macd['macd'][len(macd)-1])

    return(var)



