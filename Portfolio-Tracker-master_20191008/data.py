import quandl
import datetime as dt
import calendar
import os
import pandas as pd
import urllib
import sys
from main import root_path

#Dates
end_date = dt.date.today()
emo = end_date.month
eday = end_date.day
eyear = end_date.year
emonth = calendar.month_abbr[emo]

def portfolio(symbols, allocations, api_key, start_date):

    quandl.ApiConfig.api_key = api_key

    folders = [root_path+'/Daily Data', root_path+'/Daily Data/Portfolio', root_path+'/Daily Data/Benchmark']
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

    #Modify Symbols List
    for symbol in symbols:
        for ch in ['^', '.', '-', '/']:
            if ch in symbol:
                symbols.remove(symbol)
                symbol = symbol.replace(ch, '_')
                symbols.append(symbol)

    # Update for Quandl
    qsymbols = []
    for i in range(len(symbols)):
        qsymbol = "WIKI/" + symbols[i].upper() + ".4"
        qsymbols.append(qsymbol)

    smo = start_date.month
    sday = start_date.day
    syear = start_date.year
    smonth = calendar.month_abbr[smo]

    #Portfolio Data
    port_data = quandl.get(qsymbols, start_date=start_date, end_date=end_date, collapse="daily")
    port_data.columns = symbols

    temp_data = port_data.iloc[:,0:len(port_data.columns)].apply(pd.to_numeric)
    for column in temp_data.columns:
        c = temp_data[column]
        if c.isnull().all():
            print ('WARNING:  The following symbol: '+str(column)+' has no timeseries data. This could be due to an invalid ticker, or an entry not supported by Quandl. \n You will not be able to proceed with any function in the script until all of the symbols provided are downloaded.')
            sys.exit()

    port_val = port_data * allocations
    # Remove Rows With No Values

    #FIX!!!!!!
    #port_data.dropna(axis=0, how='any')
    port_val = port_val.fillna(port_val.mean())

    port_val['Portfolio Value'] = port_val.sum(axis=1)

    # Calculate Portfolio Returns
    port_rets = port_val.pct_change()
    port_rets = port_rets.dropna(how='any')

    #Calculate Portfolio Weights
    assets = port_val.tail(1)
    s = port_val.iloc[-1:, -1]
    port_weights = assets / int(s)
    port_weights = port_weights.transpose()
    port_weights.columns = ["Weight"]
    port_weights = port_weights.drop(port_weights.index[len(port_weights) - 1])

    port_val.to_csv(root_path+'/Daily Data/Portfolio/Portfolio Value.csv',index=True)
    port_rets.to_csv(root_path+'/Daily Data/Portfolio/Portfolio Returns.csv' ,index=True)
    port_data.to_csv(root_path+'/Daily Data/Portfolio/Portfolio Daily Prices.csv' ,index=True)
    port_weights.to_csv(root_path+'/Daily Data/Portfolio/Portfolio Weights.csv' ,index=True)

    print ('Portfolio data has successfully been downloaded.')
def benchmark(bench_symbol, start_date, api_key):

    quandl.ApiConfig.api_key = api_key

    folders = [root_path + '/Daily Data', root_path + '/Daily Data/Benchmark', root_path + '/Daily Data/Portfolio' ]
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

    smo = start_date.month
    sday = start_date.day
    syear = start_date.year
    smonth = calendar.month_abbr[smo]
    
    print ( 'http://finance.google.com/finance/historical?q='+str(bench_symbol)+'&startdate='+ str(smonth) +'+'+ str(sday) +'+'+ str(syear) +'&enddate='+ str(emonth) +'+'+ str(eday) +'+'+ str(eyear) +'&output=csv')
    #Benchmark Data
    bench_data = pd.read_csv(
        'http://finance.google.com/finance/historical?q='+str(bench_symbol)+'&startdate='+ str(smonth) +'+'+ str(sday) +'+'+ str(syear) +'&enddate='+ str(emonth) +'+'+ str(eday) +'+'+ str(eyear) +'&output=csv',
        index_col=0)["Close"]
    bench_data.index = pd.to_datetime(bench_data.index)

    #Reverse Frame
    bench_rets = bench_data.iloc[::-1]
    bench_rets = bench_rets.dropna(how='any')

    bench_rets = bench_rets.pct_change()

    bench_data.to_csv(root_path+'/Daily Data/Benchmark/Benchmark Price Data.csv' ,index=True)
    bench_rets.to_csv(root_path+'/Daily Data/Benchmark/Benchmark Returns.csv' ,index=True)
    print ( 'http://finance.google.com/finance?q='+str(bench_symbol)+'&startdate='+ str(smonth) +'+'+ str(sday) +'+'+ str(syear) +'&enddate='+ str(emonth) +'+'+ str(eday) +'+'+ str(eyear) +'&output=csv',
        index_col=0)
    print ('Benchmark data has finished downloading.')