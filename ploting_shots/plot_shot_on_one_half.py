import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen, VerticalPitch

parser = Sbopen()
df, related, freeze, tactics = parser.event(69301)
#get team names
team1, team2 = df.team_name.unique()

pitch = VerticalPitch(line_color='black', half=True)    
fig, ax = pitch.grid(grid_height=0.9, title_height= 0.06, axis=False,
                     endnote_height= 0.04, title_space= 0, endnote_space=0)

#query
mask_england = (df.type_name == 'Shot') & (df.team_name == team1)
#Finding rows in the df and keeping only necessary colums
df_england = df.loc[mask_england, ['x', 'y', 'outcome_name', 'player_name']]

#plotting all shots
pitch.scatter(df_england.x, df_england.y, s= 500, color= 'red', ax= ax['pitch'], alpha= 1, edgecolors='black')
fig.suptitle("England shots against Sweden", fontsize = 30)
plt.show()