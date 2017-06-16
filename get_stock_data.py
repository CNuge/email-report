
import numpy as np
from datetime import datetime
import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web

""" grab stock data for a suite of coumpanies I am interested in
	take this data and return a few graphs and tables. """

now = datetime.now()

start = datetime((now.year - 1), now.month, now.day)

#build a list of the stocks you care about
stocks_of_interest = ['AMZN','GOOG','AAPL','CLDR','HDP','ORCL','TSLA']

#use the below to build up a dataframe of the current price,
#a graph of the past year and a the close vs. this time a month ago
f_dat = web.DataReader(stocks_of_interest, 'google', start, now)

#then use below to get the dataframe for a specific stock
for stock in stocks_of_interest:
	f_dat.xs(stock,2)

#above works only for NYSE stocks... need to go to the source for canadian 
#ones and scrape the data from the page


canadian_stocks_of_interest = ['BEP.UN','EXE','FC','TXF','XWD','VCN','VFV','VUN']

for stock in canadian_stocks_of_interest:
#grab the web page and scrape the data


#give this one a try, amazon is out of business so old ways are done.:
https://pypi.python.org/pypi/googlefinance