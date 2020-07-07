""" This function call all of the other functions and composes the message body.

if your custom report modules are in the message folder, then the following import syntax will work:
import message.YourFile as YourFile

You can then call your functions inside the create_text_body() function using the syntax: 
YourFile.YourFunction()

"""
import message.countdowns as countdowns		#DEMO
import message.game_scores as game_scores	#DEMO
#from

def create_text_body():
	""" Call the functions that compose the email, building up the body
		of the message step by step and then appending these to """
	body_string = ''
	
	""" this section calls the demo functions and builds up the
		information I want in my email report (be aware these outputs are all strings) 
		substitute in your custom report functions here! """
	day_of_the_year = countdowns.day_of_year()	#DEMO
	day_of_my_life = countdowns.time_alive()	#DEMO
	jays_game = game_scores.get_team_result_text('Toronto Blue Jays')	#DEMO


	""" this section adds the strings to the message body
		substitute in the strings you generate here! """
	body_string += 'Countdowns:\n'				#DEMO
	body_string += day_of_the_year					#DEMO
	body_string += day_of_my_life					#DEMO
	body_string += '\n\n' #to add some separation	#DEMO

	body_string += jays_game						#DEMO
	body_string += '\n\n' #to add some separation	#DEMO
	

	return body_string #return the string to email_me.py it is then written into the email




