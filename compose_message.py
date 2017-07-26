


""" this will call all of the other functions, and compose the message
	the output of this function can then be sent via email to meself"""

import stock_data
import countdowns
import price_scrape
import game_scores
import stock_graph
from datetime import datetime

import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def create_text_body():
	""" call all the message portions """

	
	""" Call the text portions of the email, building up the body"""
	text_parts = []
	day_of_the_year = countdowns.day_of_year()
	day_of_my_life = countdowns.time_alive()
	phd_countdown = countdowns.phd_countdown()


	jays_game = game_scores.get_team_result_text('Toronto Blue Jays')

	dell_xps_2_lines = price_scrape.get_XPS_13_price()
	mac_15_2_lines = price_scrape.get_mac_15_price()
	mac_13_2_lines = price_scrape.get_mac_13_price()

	"""write the body parts to a list """
	text_parts.append('Countdowns:\n')
	text_parts.append(day_of_the_year)
	text_parts.append(day_of_my_life)
	text_parts.append(phd_countdown)
	text_parts.append('\n\n')
	text_parts.append('Computer prices:\n')
	text_parts.append(dell_xps_2_lines)
	text_parts.append(mac_15_2_lines)
	text_parts.append(mac_13_2_lines)
	text_parts.append('\n\n')
	text_parts.append(jays_game)
	text_parts.append('\n\n')
	
	"""list to a string """
	body = ''

	for i in text_parts:
		body += i


	return body


def graph_to_message_body(graph_data, message_body):
	#the default is a .png, can't explicitly specify
	graph_data.save('temp.png')

	with open('temp.png', 'rb') as fp:
		img = MIMEImage(fp.read())
		message_body.attach(img)

	os.remove('temp.png')
	return message_body


def create_stock_graphs(message_body):
	#to this point all validated as working, make the 
	#progams to graph the stock dataframes.
	#then compose the message from everything.
	now_time = datetime.now()
	start_time = datetime((now_time.year ), now_time.month - 1, now_time.day)

	#american stocks first
	stocks_of_interest = ['AMZN','GOOG','AAPL','CLDR','HDP','ORCL','TSLA']
	for stock in stocks_of_interest:
		#scrape the stock data to a df
		stock_df = stock_data.get_american_stock_dat(stock,start_time, now_time )
		#plot the stock df 
		graph_of_close = stock_graph.plot_us_stock_data(stock_df, stock)
		#take the plot and add it to the email message
		graph_to_message_body(graph_of_close, message_body)

	#then tsx stocks
	canadian_stocks_of_interest = ['BEP.UN','EXE','FC','TXF','XWD','VCN','VFV','VUN']

	for stock in canadian_stocks_of_interest:
		now = stock_data.TSE_current_price(stock)
		stock_prices.append(now)
		#scrape the stock data to a df
		price_df = stock_data.TSE_last_month_prices(stock)
		#plot the stock df 
		graph_of_close = stock_graph.plot_cad_stock_data(price_df, stock)
		#take the plot and add it to the email message
		graph_to_message_body(graph_of_close, message_body)

	return message_body






