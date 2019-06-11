from nba_api.stats.endpoints import playercareerstats
# Anthony Davis
career = playercareerstats.PlayerCareerStats(player_id='203076')
print(career.get_data_frames()[0])


from nba_api.stats.endpoints import LeagueSeasonMatchups

test = LeagueSeasonMatchups(def_team_id_nullable=1610612738)

a = test.get_dict()
a['leagueseasonmatchups']

b = test.get_data_frames()
b = b[0]


from nba_api.stats.static import teams

nba_teams = teams.get_teams()


from nba_api.stats.endpoints import LeagueGameLog

test = LeagueGameLog()
test.get_available_data()
c = test.get_data_frames()[0]
c = c[0]


