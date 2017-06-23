This is a program that sends me a few pieces of information in the morning 
when I wake up. It is modular, so new information sources can be created,
and then added to the 'compose_message.py' functions, which run all the other
modules and compose the final body of the text.

Things the program does:
1. The 'stock_data' and 'stock_graph' modules contain code that goes to google
	finance (RIP yahoo finance) and pulls the last 30 days worth of prices and 
	stores them in a pandas dataframe
	1b. I'm a good canadian boy, who as a result owns some canadian equities,
		unfortunately the pandas pandas_datareader.data can only grab historical
		stock data from american markets in .csv format... as the google finance 
		website doesn't have this info for the TSE ('Download to spreadsheet' link 
		doesn't exit? why?). So I made the two following functions for canadian stocks:

		TSE_current_price - use the google finance api to just get the current price (if thats all you want or need).
		google_historical_price_site - scrapes the data from the google finance page and parses it into a dataframe.

	These data are then graphed by 'stock_graph', and the colour changes depending
	on if the stock has gained or lost in the last 30 trading days.
2. price_scrape module looks up the prices of some laptops that I'm interested in,
	so I can see if they go on sale. note it uses the canadian prices and the 
	education prices for apple (as I'm a student and need them discounts).
3. looks up the jays score from yesterday and tells me if they won, lost, or didn't play. I'll add hockey functionality come OCT.
4. countdowns.py just gives me a few fun facts to start my day.





to do:
getting the following pandas warnings,
need to future proof the application accordingly.

/Users/Cam/anaconda3/lib/python3.6/site-packages/ggplot/utils.py:81: FutureWarning: pandas.tslib is deprecated and will be removed in a future version.
You can access Timestamp as pandas.Timestamp
  pd.tslib.Timestamp,
/Users/Cam/anaconda3/lib/python3.6/site-packages/ggplot/stats/smoothers.py:4: FutureWarning: The pandas.lib module is deprecated and will be removed in a future version. These are private functions and can be accessed from pandas._libs.lib instead
  from pandas.lib import Timestamp
/Users/Cam/anaconda3/lib/python3.6/site-packages/statsmodels/compat/pandas.py:56: FutureWarning: The pandas.core.datetools module is deprecated and will be removed in a future version. Please use the pandas.tseries module instead.
  from pandas.core import datetools
