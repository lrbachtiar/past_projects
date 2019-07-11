import pandas as pd
import numpy as np
import re

def clean_column_names(column_name):
    new_name = re.sub(r'[^A-Za-z0-9]', '_', column_name).strip()
    cameled = re.sub(r'_{1,}', '_', camel_to_lower_case(new_name))
    final = cameled[:-1] if cameled[-1] == '_' else cameled

    return final

def camel_to_lower_case(name):
    step_1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z])([0-9A-Z])', r'\1_\2', step_1).lower()

player_data = pd.read_csv('data/player_data.csv')
season_stats = pd.read_csv('data/Seasons_Stats.csv')

for c in player_data.columns:
    player_data.rename(columns={c:clean_column_names(c)}, inplace=True)

for c in season_stats.columns:
    season_stats.rename(columns={c:clean_column_names(c)}, inplace=True)

player_data.drop(columns = {'college', 'position'}, inplace = True)
player_data.dropna(inplace = True)
player_data['height_feet'], player_data['height_inches'] = player_data.height.str.split('-', 1).str
player_data['height_cm'] = player_data['height_feet'].astype(int)*30.48 + player_data['height_inches'].astype(int)*2.54
player_data['weight_kg'] = player_data['weight'].astype(int)*0.453592

season_stats.drop(columns = {'unnamed_0'}, inplace = True)

season_stats.columns = ['year', 'player', 'pos', 'age', 'tm', 'g', 'gs', 'mp', 'per', 'ts',
       '3p_ar', 'f_tr', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'usg',
       'blanl', 'ows', 'dws', 'ws', 'ws_48', 'blank_2', 'obpm', 'dbpm', 'bpm',
       'vorp', 'fg', 'fga', 'fgave', '3p', '3pa', '3pave', '2p', '2pa', '2pave', 'e_fg',
       'ft', 'fta', 'ftave', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov',
       'pf', 'pts']

total_years = season_stats['year'].unique()

test_df = season_stats[season_stats['year'] == 1995]

yoy_3p = season_stats.groupby(['year']).agg({'3p': 'sum', '3pa': 'sum'})
yoy_3p['3pave'] = yoy_3p['3p']/yoy_3p['3pa']
