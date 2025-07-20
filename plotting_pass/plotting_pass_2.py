#importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen

parser = Sbopen()
df, related, freeze, tactics = parser.event(69301)
mask_bronze = (df.type_name == 'Pass') & (df.player_name == 'Lucy Bronze')
df_passes = df.loc[mask_bronze, ['x', 'y', 'end_x', 'end_y']]

#drawing the pitch
pitch = Pitch(line_color="black")
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                   endnote_height=0.04, title_space=0, endnote_space=0)

#plotting the passes
pitch.arrows(df_passes.x, df_passes.y, df_passes.end_x, df_passes.end_y, color='blue', ax=ax['pitch'])
pitch.scatter(df_passes.x, df_passes.y, alpha=0.2, s= 500, color='blue', ax=ax['pitch'])
fig.suptitle("Lucy Bronze's passes against Sweden", fontsize=30)
plt.show()