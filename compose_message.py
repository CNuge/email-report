


""" this will call all of the other functions, and compose the message
	the output of this function can then be sent via email to meself"""

import stock_data
import countdowns
import price_scrape
import game_scores
import stock_graph
from datetime import datetime

def build_email():
	""" call all the message portions """

	
	""" don't need to leave these as variables
		if cleaner to do otherwise, just storing
		so I don't forget them all! """
	day_of_the_year = countdowns.day_of_year()
	day_of_my_life = countdowns.time_alive()
	phd_countdown = countdowns.phd_countdown()

	dell_xps_2_lines = price_scrape.get_XPS_13_price()
	mac_15_2_lines = price_scrape.get_mac_15_price()
	mac_13_2_lines = price_scrape.get_mac_13_price()

	jays_game = game_scores.get_team_result_text('Toronto Blue Jays')


	#to this point all validated as working, make the 
	#progams to graph the stock dataframes.
	#then compose the message from everything.
	now_time = datetime.now()
	start_time = datetime((now_time.year ), now_time.month - 1, now_time.day)

	stocks_of_interest = ['AMZN','GOOG','AAPL','CLDR','HDP','ORCL','TSLA']

	for stock in stocks_of_interest:
		stock_df = stock_data.get_american_stock_dat(stock,start_time, now_time )
		#plot the stock df and return the newest
		graph_of_close = stock_graph.plot_us_stock_data(stock_df, stock)
	#above works only for NYSE stocks... need to go to the source for canadian 
	#ones and scrape the data from the page


	canadian_stocks_of_interest = ['BEP.UN','EXE','FC','TXF','XWD','VCN','VFV','VUN']
	stock_prices = []
	for stock in canadian_stocks_of_interest:
		now = stock_data.TSE_current_price(stock)
		stock_prices.append(now)

		price_df = stock_data.TSE_last_month_prices(stock)

		graph_of_close = stock_graph.plot_cad_stock_data(price_df, stock)







