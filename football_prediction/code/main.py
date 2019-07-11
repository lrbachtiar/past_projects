import sqlite3
import pandas as pd

from functions import get_fifa_data

conn = sqlite3.connect('../input/database.sqlite')

#Fetching required data tables
player_data = pd.read_sql_query("SELECT * FROM Player;", conn)
player_stats_data = pd.read_sql("SELECT * FROM Player_Attributes;", conn)
team_data = pd.read_sql("SELECT * FROM Team;", conn)
match_data = pd.read_sql("SELECT * FROM Match;", conn)
conn.close()

#Reduce match data to fulfill run time requirements
rows = ["country_id", "league_id", "season", "stage", "date", "match_api_id", "home_team_api_id", 
        "away_team_api_id", "home_team_goal", "away_team_goal", "home_player_1", "home_player_2",
        "home_player_3", "home_player_4", "home_player_5", "home_player_6", "home_player_7", 
        "home_player_8", "home_player_9", "home_player_10", "home_player_11", "away_player_1",
        "away_player_2", "away_player_3", "away_player_4", "away_player_5", "away_player_6",
        "away_player_7", "away_player_8", "away_player_9", "away_player_10", "away_player_11"]
match_data.dropna(subset = rows, inplace = True)
match_data = match_data.tail(100)
#player_stats_data = player_stats_data.tail(30)

## Generating features, exploring the data, and preparing data for model training
#Generating or retrieving already existant FIFA data
fifa_data = get_fifa_data(match_data, player_stats_data, data_exists = False)

