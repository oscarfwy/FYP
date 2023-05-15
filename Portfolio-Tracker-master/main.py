#------------Necessary Variables--------------#
import datetime as dt
symbols = ['BA', 'MSFT', 'MMM', 'JNJ', 'JPM', 'AXP', 'IBM', 'KO', 'HD', 'GE']
allocations = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
start_date = dt.date(2019,1,1)

#Benchmark Index
bench_symbol = "SPY"

#RF Syntax: 6 MO, 2 YR etc.
rate = '1 YR'
#CUR, AVG
method = "AVG"

#For Quandl
api_key = "FZwTLC8kUGCegX2aEFKK"

#Dirctory Input For Data and Reports
root_path = "E:/MyStuff/Documents/FinTech/Portfolio-Tracker-master"

#------------Run Program----------------------#
if __name__ == '__main__':
    import rebalance
    #rebalance.rebalance(allocations=allocations)
     # 1.) Import the module
    import report
    
    # # Select Functions
    #end_date = dt.date.today()

    #r = report.rep(fname=root_path + '/Reports/Daily Report ' + str(end_date) + '.pdf',fund_name="Valhalla Investments LLC",logo_path="E:\MyStuff\Documents\FinTech\Portfolio-Tracker-master/image/logo.png")
    #r.cover()
    #r.perf()
    #r.mets()
    #r.diversification()
    #r.savePDF()

    import data as da

    #da.portfolio(symbols, allocations, api_key, start_date)
    da.benchmark(bench_symbol,start_date,api_key)