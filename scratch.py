import pandas as pd
from pandas_datareader import data
import datetime
import qqpat

#demonstrating the tool that pulls from yahoo
aapl = data.DataReader('AAPL','yahoo',start=datetime.datetime(2016, 1, 1),end=datetime.datetime.now())
spy = data.DataReader('SPY', 'yahoo', start=datetime.datetime(2016, 1, 1), end=datetime.datetime.now())
ibm = data.DataReader('IBM', 'yahoo', start=datetime.datetime(2016, 1, 1), end=datetime.datetime.now())

#showing the columns
aapl.dtypes

#ndarray of the indices which in this case are the stock dates
aapl.index.values

#gives the dimension, as expected is just 1d and has the total dates.
#as of feb 11 2018 this value is 531
#can it be estimated as 5/7 of the date difference between start and end of the pull?
aapl.index.values.shape

#seeing if 531 can be estimated by me
#close enough i guess, maybe holidays get left out, not looking it up right now
start=datetime.datetime(2016, 1, 1)
start=datetime.datetime(2018, 2, 11)
date_delta = datetime.datetime(2018, 2, 11) - datetime.datetime(2016, 1, 1)
date_delta.days*float(5)/7

#next is printing the dates to excel.  this will help me evalauate how concatenate is working hoping that they don't perfectly share all of the indices.  does it kick out indices that don't match?
ibm.to_csv('G:\\PyCharm Projects\\asset_analysis\\ibm.csv')
data = pd.concat([aapl['Close'], spy['Close'], ibm['Close']], axis=1)
data.to_csv('G:\\PyCharm Projects\\asset_analysis\\data.csv')

analyzer = qqpat.Analizer(data, column_type='price', titles=["APPL", "SPY", "IBM"])
summary = analyzer.get_statistics_summary()

#is a list for each stock price column of different statistics
type(summary)

#dictionary with the statsitics for a given column (stock)
type(summary[0])

#list with metric names
type(summary[0].keys())

print('for break')

analyzer.plot_analysis_returns()
analyzer.min_variance_portfolio_optimization(plotWeights=True)

analyzer.plot_mc_wc_evolution_sharpe(index=0, iterations=50, confidence=99, max_period_length=1000)
analyzer.plot_mc_wc_evolution_cagr(index=0, iterations=50, confidence=99, max_period_length=1000)

analyzer.plot_mc_distributions(index=0, iterations=100)
analyzer.plot_mc_simulations(index=0, iterations=100)

analyzer.plot_analysis_rolling()
analyzer.plot_monthly_returns_heatmap()
analyzer.plot_annual_returns()
analyzer.plot_monthly_returns()
analyzer.plot_annual_returns()
analyzer.plot_monthly_return_distribution()

analyzer.plot_drawdown_periods()
analyzer.plot_drawdown_distribution()
analyzer.plot_drawdown_length_distribution()



