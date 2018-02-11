from pandas_datareader import data
import datetime

#demonstrating the tool that pulls from yahoo
aapl = data.DataReader('AAPL','yahoo',start=datetime.datetime(2016, 1, 1),end=datetime.datetime.now())

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
