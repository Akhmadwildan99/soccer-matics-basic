import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen
import pandas as pd

parser = Sbopen()
df, related, freeze, tactics = parser.event(69301)

#check for index of first sub
sub= df.loc[df["type_name"] == "Substitution"].loc[df["team_name"] == "England Women's"].iloc[0]["index"]
print(f"First substitution index: {sub}")
#filter passes
mask_england = (df.type_name == 'Pass') & (df.team_name == "England Women's")& (df.index < sub) & (df.outcome_name.isnull()) & (df.sub_type_name != "Throw-in")
df_passes = df.loc[mask_england, ['x', 'y', 'end_x', 'end_y', 'player_name', 'pass_recipient_name']]
# print(f"Number of passes:\n{len(df_passes)}")
# print(f"First 5 passes:\n{df_passes.get('player_name').head()}")

#adjusting that only the surname of a player is presented.
df_passes["player_name"] = df_passes["player_name"].apply(lambda x: x.split()[-1])
df_passes["pass_recipient_name"] = df_passes["pass_recipient_name"].apply(lambda x: str(x).split()[-1])
# print diff df_passes["player_name"] and df_passes["player_name"].apply(lambda x: x.split()[-1])
# print(f"First 5 passes after adjustment:\n{df_passes.get('player_name').head()}")
# print(f"First 5 pass recipients after adjustment:\n{df_passes.get('pass_recipient_name').head()}")


scatter_df = pd.DataFrame()
for i, name in enumerate(df_passes["player_name"].unique()):
    passx = df_passes.loc[df_passes["player_name"] == name]["x"].to_numpy()
    recx = df_passes.loc[df_passes["pass_recipient_name"] == name]["end_x"].to_numpy()
    passy = df_passes.loc[df_passes["player_name"] == name]["y"].to_numpy()
    recy = df_passes.loc[df_passes["pass_recipient_name"] == name]["end_y"].to_numpy()
    scatter_df.at[i, "player_name"] = name
    #make sure that x and y location for each circle representing the player is the average of passes and receptions
    scatter_df.at[i, "x"] = np.mean(np.concatenate([passx, recx]))
    scatter_df.at[i, "y"] = np.mean(np.concatenate([passy, recy]))
    #calculate number of passes
    scatter_df.at[i, "no"] = df_passes.loc[df_passes["player_name"] == name].count().iloc[0]


#adjust the size of a circle so that the player who made more passes
scatter_df['marker_size'] = (scatter_df['no'] / scatter_df['no'].max()  *1500)

print(f"Scatter dataframe:\n{scatter_df}")
#counting passes between players
df_passes["pair_key"]= df_passes.apply(lambda x: "_".join(sorted([x["player_name"], x["pass_recipient_name"]])), axis=1)
# print(f"First 5 pair keys:\n{df_passes.get('pair_key').head()}")
lines_df = df_passes.groupby(["pair_key"]).x.count().reset_index()
# print(f"Lines dataframe:\n{lines_df.head()}")
lines_df.rename({'x':'pass_count'}, axis='columns', inplace=True)
lines_df= lines_df[lines_df['pass_count'] > 2]
# print(f"Lines dataframe after filtering:\n{lines_df.head()}")
#counting number of passes between players



#Drawing pitch
pitch = Pitch(line_color='grey')
fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                     endnote_height=0.04, title_space=0, endnote_space=0)

#Scatter the location on the pitch
pitch.scatter(scatter_df.x, scatter_df.y, s=scatter_df.marker_size, color='red', edgecolors='grey', linewidth=1, alpha=1, ax=ax["pitch"], zorder = 3)

#annotating player name
for i, row in scatter_df.iterrows():
    pitch.annotate(row['player_name'], xy= (row['x'], row['y']), c='black', va='center', ha='center',  weight = "bold", size=16, ax=ax['pitch'], zorder=4)
# plt.show()
#Plotting lines between players
for i, row in lines_df.iterrows():
    player1 = row["pair_key"].split("_")[0]
    player2 = row['pair_key'].split("_")[1]
    #take the average location of players to plot a line between them
    player1_x = scatter_df.loc[scatter_df['player_name'] == player1]['x'].iloc[0]
    player1_y = scatter_df.loc[scatter_df['player_name'] == player1]['y'].iloc[0]
    player2_x = scatter_df.loc[scatter_df['player_name'] == player2]['x'].iloc[0]
    player2_y = scatter_df.loc[scatter_df['player_name'] == player2]['y'].iloc[0]
    num_passes = row["pass_count"]
    #adjust the line width so that the more passes, the wider the line
    line_width = (num_passes / lines_df['pass_count'].max() * 10)
    pitch.lines(player1_x, player1_y, player2_x, player2_y, alpha=1, lw=line_width, zorder=2, color="red", ax = ax["pitch"])


fig.suptitle("Nodes location - England", fontsize = 30)
plt.show()


#calculate number of successful passes by player
no_passes = df_passes.groupby(['player_name']).x.count().reset_index()
no_passes.rename({'x':'pass_count'}, axis='columns', inplace=True)
#find one who made most passes
max_no = no_passes["pass_count"].max()
print(f"Number of passes by player:\n{no_passes} \nMax number of passes: {max_no}")
#calculate the denominator - 10*the total sum of passes
denominator = 10*no_passes["pass_count"].sum()
#calculate the nominator
nominator = (max_no - no_passes["pass_count"]).sum()
print(f"Denominator: {denominator}, Nominator: {nominator}")
#calculate the centralisation index
centralisation_index = nominator/denominator
print("Centralisation index is ", centralisation_index)