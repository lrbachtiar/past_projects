# =============================================================================
# Import Libraries
# =============================================================================
import pandas as pd
import numpy as np

import seaborn as sns

from sklearn.model_selection import train_test_split

from nba_api.stats.endpoints import LeagueGameLog
from nba_api.stats.static import teams

# =============================================================================
# Functions
# =============================================================================

# function for creating a feature importance dataframe
def imp_df(column_names, importances):
    df = pd.DataFrame({'feature': column_names,
                       'feature_importance': importances}) \
           .sort_values('feature_importance', ascending = False) \
           .reset_index(drop = True)
    return df

# plotting a feature importance dataframe (horizontal barchart)
def var_imp_plot(imp_df, title):
    imp_df.columns = ['feature', 'feature_importance']
    sns.barplot(x = 'feature_importance', y = 'feature', data = imp_df, orient = 'h', color = 'royalblue') \
       .set_title(title, fontsize = 20)

# =============================================================================
# Prepare Data
# =============================================================================

nba_teams = teams.get_teams()

df_matchups = LeagueGameLog().get_data_frames()[0]

matchup_dets= df_matchups['MATCHUP'].str.split(' ', n = 2, expand = True) 
matchup_dets = matchup_dets.rename(columns = {0: 'TEAM', 1: 'HOME_AWAY', 2: 'OPPONENT'})
matchup_dets['HOME_AWAY'] = np.where(matchup_dets['HOME_AWAY'] == 'vs.', 1, 0)

df_matchups = pd.concat([df_matchups, matchup_dets], axis=1)
df_matchups['RESULT'] = np.where(df_matchups['WL'] == 'W', 1, 0)

nba_teams['abbreviation' == 'WAS']['id']

df_nba_teams = pd.DataFrame(nba_teams)
df_nba_teams = df_nba_teams.rename(columns = {'id': 'OPPONENT_ID', 'abbreviation': 'OPPONENT_NAME'})

df_matchups = pd.merge(df_matchups, df_nba_teams[['OPPONENT_ID', 'OPPONENT_NAME']], left_on = 'OPPONENT', right_on = 'OPPONENT_NAME', how = 'left')

cols = ['SEASON_ID',
        'TEAM_ID',
#        'GAME_ID',
#        'GAME_DATE',
        'MIN',
        'FGM',
        'FGA',
        'FG_PCT',
        'FG3M',
        'FG3A',
        'FG3_PCT',
        'FTM',
        'FTA',
        'FT_PCT',
        'OREB',
        'DREB',
        'REB',
        'AST',
        'STL',
        'BLK',
        'TOV',
        'PF',
#        'PTS',
#        'PLUS_MINUS',
#        'TEAM',
        'HOME_AWAY',
        'OPPONENT_ID']

y = df_matchups['RESULT']
X = df_matchups[cols]

np.random.seed(seed = 42)

X['random'] = np.random.random(size = len(X))
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size = 0.8, random_state = 42)

sns.scatterplot(x = 'random', y = 'target', data = X.assign(target = y)).set_title('Random feature vs. target variable', fontsize = 16)
sns.heatmap(X.assign(target = y).corr().round(2), cmap = 'Blues', annot = True).set_title('Correlation matrix', fontsize = 16)

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators = 100,
                           n_jobs = -1,
                           oob_score = True,
                           bootstrap = True,
                           random_state = 42)
rf.fit(X_train, y_train)

print('R^2 Training Score: {:.2f} \nOOB Score: {:.2f} \nR^2 Validation Score: {:.2f}'.format(rf.score(X_train, y_train), 
                                                                                    rf.oob_score_,
                                                                                    rf.score(X_valid, y_valid)))

base_imp = imp_df(X_train.columns, rf.feature_importances_)
print(base_imp)

var_imp_plot(base_imp, 'Default feature importance (scikit-learn)')
