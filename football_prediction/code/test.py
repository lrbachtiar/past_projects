import sqlite3
conn = sqlite3.connect('../input/database.sqlite')
player_data = pd.read_sql_query("SELECT * FROM Player;", conn)
