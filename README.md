# Cam's Morning report

This is a program that sends me a few pieces of information in the morning 
when I wake up. It is modular, so new information sources can be created,
and then added to the 'compose_message.py' functions, which run all the other
modules and compose the final body of the text.

Things the program does:
1. The 'stock_data' and 'stock_graph' modules contain code that goes to google
	finance and pulls the last 30 days worth of prices and stores them in a pandas dataframe
	Please note: scraping stock data is a changing landscape, Yahoo Finance is once
	again working, but I use the old code I wrote here mainly as a test to see how
	long the beautiful soup scraper can run before it breaks
2. price_scrape module looks up the prices of some laptops that I'm interested in,
	so I can see if they go on sale. note it uses the canadian prices and the 
	education prices for apple (as I'm a student and need them discounts).
3. game_scores.py looks up the blue jays score from yesterday and tells me if they won, lost, or didn't play.
4. countdowns.py just gives me a few fun facts to start my day (based on the datetime module).

## To run this program:
You need to hook it up to an email address in the email_me.py file (so that it can send the message from somewhere). These fields are currently stars so that you can't get into my email.

With an email set up you need the following installed:

	pip install pandas
	pip install bs4 #BeautifulSoup
	pip install ggplot
