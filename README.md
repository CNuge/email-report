# Cam's Morning report



goal: take the existing email notification repository and update it for other people
to use

Current flat file structure:
| morning_report
	stock_graph.py
	stock_data.py
	README.md
	price_scrape.py
	LICENSE
	game_scores.py
	email_me.py
	countdowns.py
	compose_message.py

Want to change it to the following:

| email_report
	README.md
	LICENSE
	email_me.py
	| message
		__init__.py
		compose_message.py
		example_countdowns.py
		example_game_scores.py

Write the readme so it explains to people how to do the following:
1. Hook the email_me.py up to their own email so it will send
2. write new data scrapers or countdowns and add them to the message folder
3. alter the compose message to import and use the new message components
4. Give a description of how you can have the message auto send
	crontab -e
	Then you want to add:

	0 5 * * 1-5 python email_me.py

make the readme descriptive enough for others to alter the program. Encourage others this
is a fun way to practice and apply some simple web scrpaing tasks. Easy to change
and very customizable. 








This is a program that sends me a few pieces of information in the morning 
when I wake up. It is modular, so new information sources can be created,
and then added to the 'compose_message.py' functions, which run all the other
modules and compose the final body of the text.

Things the program does:
1. The 'stock_data' and 'stock_graph' modules contain code that goes to google
	finance and pulls the last 30 days worth of prices and stores them in a pandas dataframe.
	
	Please note: scraping stock data is a changing landscape, Yahoo Finance is once
	again working, but I use the old code I wrote here mainly as a test to see how
	long the beautiful soup scraper can run before it breaks!

2. price_scrape module looks up the prices of some laptops that I'm interested in,
	so I can see if they go on sale. Note: it uses the canadian prices and the 
	education prices for apple (as I'm a student and need them discounts).

3. game_scores.py looks up the blue jays score from yesterday and tells me if they won, lost, or didn't play.

4. countdowns.py just gives me a few fun facts to start my day (based on the datetime module).

## To run this program:
You need to hook it up to an email address in the email_me.py file (so that it can send the message from somewhere). These fields are currently stars so that you can't get into my email.

With an email set up you need the following installed:

	pip install pandas
	pip install bs4 #BeautifulSoup
	pip install ggplot

Then to run the program all you need to do is:

	python email_me.py
	
The program will then scrape all the necessary data, build the required graphs and send you an email!
I set this up using a cron shell script so that it auto-runs on AWS every weekday morning, and then I get my morning report automatically!
