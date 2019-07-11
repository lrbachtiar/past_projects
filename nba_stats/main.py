import pandas as pd

from nba_api.stats.static import teams
from nba_api.stats.endpoints import LeagueGameLog, PlayerGameLog

from functions import create_connection,\
                        clean_column_names

# Create database connection
conn = create_connection('database.db')

# Get list of NBA teams
nba_teams = pd.DataFrame(teams.get_teams())

# Get list of historical regular season matchups
season_matchups = pd.DataFrame()
season_list = list(range(2003, 2019))
for i in range(0, len(season_list)-1):
    get_year = str(season_list[i]) + '-' + str(season_list[i+1])[2:]
    print(get_year)
    temp = LeagueGameLog(season=get_year, season_type_all_star='Regular Season').get_data_frames()[0]
    season_matchups = season_matchups.append(temp)

for c in season_matchups.columns:
    season_matchups.rename(columns={c:clean_column_names(c)}, inplace=True)

# Write to SQL database
nba_teams.to_sql(name='teams', con=conn, index=False, if_exists='replace')
season_matchups.to_sql(name='season_matchups', con=conn, index=False, if_exists='replace')

conn.close()

#player_gamelogs = PlayerGameLog().get_data_frames()[0]