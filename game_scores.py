from urllib.request import urlopen
from bs4 import BeautifulSoup

""" go through the tsn website, return the game scores, and links to games involving teams
	that you care about. """


""" mlb """
def get_mlb_team_score(query_team):
	""" put in the long for name of the team of interest:
		i.e. 'Toronto Blue Jays', 'New York Yankees' """
	baseball_reference = 'http://www.baseball-reference.com/'

	mlb_dat = urlopen(baseball_reference)

	mlb_scores= BeautifulSoup(mlb_dat, 'lxml')

	game_section = mlb_scores.find(id="scores")

	yesterday_games = game_section.findAll('',{'class','teams'})

	for game in yesterday_games:
		winner=game.find('',{'class':'winner'})
		w_team = winner.td.get_text()
		loser =game.find('',{'class':'loser'})
		l_team = loser.td.get_text()
		if (w_team != query_team) and (l_team != query_team):
			continue
		else:
			w_score = winner.find('',{'class':'right'}).get_text()
			l_score = loser.find('',{'class':'right'}).get_text()

			return {w_team:w_score,l_team:l_score}
	return 'did not play yesterday'



#team = 'Toronto Blue Jays'
def get_team_result_text(team):
	yesterday_game = get_mlb_team_score(team)
	if yesterday_game == 'did not play yesterday':
		return 'The %s %s.' % (team, yesterday_game)
	else:
		other_team = [z for z in yesterday_game.keys() if z != team][0]
		team_score = yesterday_game[team]
		other_team_score = yesterday_game[other_team]
		if int(team_score) < int(other_team_score):
			result = 'Yesterday, the %s lost to the %s, %s-%s.' % (team,other_team,other_team_score,team_score)
			return result
		else:
			result = 'Yesterday, the %s beat the %s, %s-%s.' % (team,other_team,team_score,other_team_score)
			return result




