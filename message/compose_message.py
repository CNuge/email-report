


""" this will call all of the other functions, and compose the message
	the output of this function can then be sent via email to meself"""

# if your custom report modules are in the message folder, then the following
# import syntax will work
# import message.YourFile as YourFile
# then you can call your functions here using: YourFile.YourFunction()

import message.countdowns as countdowns		#DEMO
import message.game_scores as game_scores	#DEMO



def create_text_body():
	""" Call the functions that compose the email, building up the body
		of the message step by step and then appending these to """
	body_string = ''
	
	""" this section calls the demo functions and builds up the
		information I want in my email report (be aware these outputs are all strings) 
		substitute in your custom report functions here! """
	day_of_the_year = countdowns.day_of_year()	#DEMO
	day_of_my_life = countdowns.time_alive()	#DEMO
	phd_countdown = countdowns.phd_countdown()	#DEMO
	jays_game = game_scores.get_team_result_text('Toronto Blue Jays')	#DEMO


	""" this section adds the strings to the message body
		substitute in the strings you generate here! """
	text_parts.append('Countdowns:\n')				#DEMO
	body_string += day_of_the_year					#DEMO
	body_string += day_of_my_life					#DEMO
	body_string += '\n\n' #to add some separation	#DEMO

	body_string += 'jays_game'						#DEMO
	body_string += '\n\n' #to add some separation	#DEMO
	

	return body_string #return the string to email_me.py it is then written into the email




