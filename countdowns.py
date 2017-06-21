
from datetime import datetime


""" these functions count out a few fun time facts for me
	day of my life, int(day of the year) and also time to go in my phd
	(aggressive timeline)"""

	
def day_of_year(now=datetime.now()):
	day_of_the_year = now - datetime(now.year, 1, 1) 
	date_summary = 'Today is day number %d of %d' % (day_of_the_year.days, now.year)
	return date_summary

def time_alive(now=datetime.now()):
	your_life = now - datetime(****)
	len_existence = 'Today is day number %d of your life' % (your_life.days)
	return len_existence


def phd_countdown(now = datetime.now()):
	finish_phd = datetime(****)
	days_to_go = finish_phd - now
	get_er_done = 'You have %d days to finish your phd! Get to work.' % (days_to_go.days)
	return get_er_done

