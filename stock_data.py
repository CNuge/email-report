
from datetime import datetime
from pandas import DataFrame
import pandas_datareader.data as web
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

""" grab stock data for a suite of coumpanies I am interested in
	take this data and return a few graphs and tables. """

#build a list of the stocks you care about

def get_american_stock_dat(stock_of_interest, start_time, now_time):
	""" get a dataframe for an american stock of interest """
	f_dat = web.DataReader(stock_of_interest, 'google', start_time, now_time)
	return f_dat

def TSE_current_price(stock):
	google_price_api = 'http://finance.google.com/finance/info?client=ig&q=TSE%3A'
	current_price_api = google_price_api+stock
	stock_dat_now = urlopen(current_price_api)
	now_price = BeautifulSoup(stock_dat_now, 'lxml')
	dict_string = [x for x in now_price.body.p.children][0]
	t_1 = dict_string.split('[\n')[1]
	t_2 = t_1.split('\n]')[0]
	parsed_now_price = json.loads(t_2)

	# 't' is ticker name
	# 'l' == last price
	return (parsed_now_price['t'], parsed_now_price['l'])

def TSE_last_month_prices(stock):
	""" return a dataframe with the dates and the closing prices """
	google_historical_price_site= 'https://www.google.ca/finance/historical?q=TSE%3A'
	historical_price_page = google_historical_price_site + stock
	stock_dat = urlopen(historical_price_page)
	#then parse the tbale with BS and call the next page with the crawler

	historical_page = BeautifulSoup(stock_dat,'lxml')

	table_dat = historical_page.find('table',{'class':'gf-table historical_price'})

	rows = table_dat.findAll('td',{'class':'lm'})
	dates = [x.get_text().rstrip() for x in rows]
	datetime_dates = [datetime.strptime(x, '%b %d, %Y') for x in dates]
	prices = []
	for num, row in enumerate(rows):
		row_dat = [datetime_dates[num]] #first column is the dates
		for i in row.next_siblings: 
			row_dat.append(i.get_text().rstrip()) #iterate through columns, append
		prices.append(row_dat) #add the row to the list of rows

	outdat = DataFrame(prices,columns = ['Date','Open','High','Low','Close','Volume'])
	
	outdat["Volume"] = outdat["Volume"].apply(lambda x: int(x.replace(',','')))
	outdat.set_index('Date')
	return outdat

def international_last_month_prices(market, stock):
	""" return a historical stock dataframe for any market and any stock """
	google_historical_price_site= 'https://www.google.ca/finance/historical?q='
	historical_price_page = google_historical_price_site+market+'%3A'+stock
	stock_dat = urlopen(historical_price_page)
	#then parse the table with BS 
	historical_page = BeautifulSoup(stock_dat,'lxml')
	table_dat = historical_page.find('table',{'class':'gf-table historical_price'})
	rows = table_dat.findAll('td',{'class':'lm'})
	dates = [x.get_text().rstrip() for x in rows]
	#get datetime formatted dates
	datetime_dates = [datetime.strptime(x, '%b %d, %Y') for x in dates]
	prices = []
	#iterate and grab column data
	for num, row in enumerate(rows):
		row_dat = [datetime_dates[num]] #first column is the dates
		for i in row.next_siblings: 
			row_dat.append(i.get_text().rstrip()) 
		prices.append(row_dat) #add the row to the list of rows
	outdat = DataFrame(prices,columns = ['Date','Open','High','Low','Close','Volume'])
	#cleanup, set index and make volume integers
	outdat["Volume"] = outdat["Volume"].apply(lambda x: int(x.replace(',','')))
	#change the other columns to floating point values
	for col in ['Open','High','Low','Close']:
		outdat[col] = outdat[col].apply(lambda x: float(x))
	outdat = outdat.set_index('Date')
	outdat = outdat.sort_index() #sort the index so it is oldest to newest
	return outdat


if __name__ == '__main__':

	now_time = datetime.now()

	if now_time.month != 1:
		start_time = datetime(now_time.year , now_time.month - 1, now_time.day)
	else:
		start_time = datetime(now_time.year -1 , 12, now_time.day)
	
	stocks_of_interest = ['AMZN','GOOG','AAPL','CLDR','HDP','ORCL','TSLA']

	for stock in stocks_of_interest:
		#scrape the stock data to a df
		stock_df = get_american_stock_dat(stock,start_time, now_time )
		#plot the stock df 
		graph_of_close = stock_graph.plot_us_stock_data(stock_df, stock)
		#take the plot and add it to the email message
		graph_to_message_body(graph_of_close, message_body)



	canadian_stocks_of_interest = ['BEP.UN','EXE','FC','TXF','XWD','VCN','VFV','VUN']
	
	stock_prices = []
	for stock in canadian_stocks_of_interest:
		now = TSE_current_price(stock)
		stock_prices.append(now)
		#scrape the stock data to a df
		price_df = TSE_last_month_prices(stock)
		#plot the stock df 
		graph_of_close = stock_graph.plot_cad_stock_data(price_df, stock)
		#take the plot and add it to the email message
		graph_to_message_body(graph_of_close, message_body)









