import pandas as pd
from pandas_datareader import data
import datetime
import qqpat

aapl = data.DataReader('AAPL', 'yahoo', start=datetime.datetime(2016, 1, 1), end=datetime.datetime.now())

spy = data.DataReader('SPY', 'yahoo', start=datetime.datetime(2016, 1, 1), end=datetime.datetime.now())

ibm = data.DataReader('IBM', 'yahoo', start=datetime.datetime(2016, 1, 1), end=datetime.datetime.now())

data = pd.concat([aapl['Close'], spy['Close'], ibm['Close']], axis=1)

analyzer = qqpat.Analizer(data, column_type='price', titles=["APPL", "SPY", "IBM"])

summary = analyzer.get_statistics_summary()

for idx, statistics in enumerate(summary):
    print ""
    print "statistics for system {}:".format(idx)
    for s in statistics:
        print "{}: {}".format(s, summary[idx][s])
    print ""

print('for break')

analyzer.plot_analysis_returns()

print('for break')