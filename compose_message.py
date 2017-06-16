


""" this will call all of the other functions, and compose the message
	the output of this function can then be sent via email to meself"""


import countdowns
import price_scrape

def build_email():
	""" call all the message portions """

	
	""" don't need to leave these as variables
		if cleaner to do otherwise, just storing
		so I don't forget them all! """
	day_of_the_year = countdowns.day_of_year()
	day_of_my_life = countdowns.time_alive()
	phd_countdown = countdowns.phd_countdown()

	dell_xps_2_lines = get_XPS_13_price()
	mac_15_2_lines = get_mac_15_price()
	mac_13_2_lines = get_mac_13_price()

	jays_game = get_team_result_text('Toronto Blue Jays')