
from datetime import datetime


""" these functions count out a few fun time facts for me
	day of my life, int(day of the year) and also time to go in my phd
	(aggressive timeline)"""

	
def day_of_year(now=datetime.now()):
	day_of_the_year = now - datetime(now.year -1, 12, 31) 
	date_summary = 'Today is day number %d of the year %d.\n' % (day_of_the_year.days, now.year)
	return date_summary

def time_alive(now=datetime.now()):
	your_life = now - datetime(1970, 1, 1)
	len_existence = 'Today is day number %d of your life.\n' % (your_life.days)
	return len_existence

