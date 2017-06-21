from ggplot import *


def plot_cad_stock_data(price_df, company_name):
	""" takes in a stock df with columns 'Date' and 'Close' """
	price_df['Close'] = [float(x) for x in price_df['Close']]
	price_df['num_days'] = price_df.index
	if price_df['Close'][0] < price_df['Close'][len(price_df['Close'])-1]:
		colour = 'green'
	else:
		colour = 'red'
	title = '%s closing price - last 30 trading days' % (company_name)
	stock_graph = ggplot(aes(x='num_days',y='Close'), data = price_df) + \
		geom_line() + \
		xlab('days') + \
		ylab('price (CAD)') + \
		ggtitle(title) + \
		ylim( (price_df['Close'].min() -1),(price_df['Close'].max() +1))  + \
		geom_area(aes(x='num_days',y='Close'),fill=colour, data = price_df)
	return stock_graph


def plot_us_stock_data(price_df, company_name):
	""" takes in a stock df with column Close' """
	price_df['num_days'] = [x for x , y in enumerate(price_df['Close'])]
	if price_df['Close'][0] < price_df['Close'][len(price_df['Close'])-1]:
		colour = 'green'
	else:
		colour = 'red'
	title = '%s closing price - last 30 trading days' % (company_name)
	stock_graph = ggplot(aes(x='num_days',y='Close'), data = price_df) + \
		geom_line() + \
		xlab('days') + \
		ylab('price (USD)') + \
		ggtitle(title) + \
		ylim( (price_df['Close'].min() -1),(price_df['Close'].max() +1))  + \
		geom_area(aes(x='num_days',y='Close'),fill=colour, data = price_df)
	return stock_graph



