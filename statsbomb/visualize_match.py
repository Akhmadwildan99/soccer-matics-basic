from mplsoccer import Sbopen, Pitch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Initialize the parser
parser = Sbopen()

# Load the Champions League final match
competition_id = 16  # Champions League
season_id = 4  # 2018/2019 season
df_matches = parser.match(competition_id=competition_id, season_id=season_id)

# Get the match ID for the final (there's only one match)
match_id = df_matches.iloc[0]['match_id']
home_team = df_matches.iloc[0]['home_team_name']
away_team = df_matches.iloc[0]['away_team_name']
print(f"Visualizing shots from {home_team} vs {away_team}")

# Load event data for this match
df_events, related_events, freeze_frame, tactics = parser.event(match_id)

# Filter for shots
shots = df_events[df_events['type_name'] == 'Shot'].copy()
print(f"Total shots in match: {len(shots)}")

# Count shots by team
home_shots = shots[shots['team_name'] == home_team]
away_shots = shots[shots['team_name'] == away_team]
print(f"{home_team}: {len(home_shots)} shots")
print(f"{away_team}: {len(away_shots)} shots")

# Find goals (shots with outcome_name = 'Goal')
if 'outcome_name' in shots.columns:
    goals = shots[shots['outcome_name'] == 'Goal']
    print(f"\nGoals scored: {len(goals)}")
    for _, goal in goals.iterrows():
        print(f"Goal by {goal['player_name']} ({goal['team_name']})")

# Setup the pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color='grass', line_color='white')
fig, ax = pitch.draw(figsize=(16, 11))
fig.set_facecolor('white')

# Plot the shots
for team, color in zip([home_team, away_team], ['blue', 'red']):
    team_shots = shots[shots['team_name'] == team]
    
    # Plot the shot locations
    if 'shot_statsbomb_xg' in shots.columns:
        # Use xG for size if available
        pitch.scatter(team_shots.x, team_shots.y, s=team_shots.shot_statsbomb_xg * 900 + 100,
                    color=color, edgecolors='black', linewidth=1, alpha=0.7, ax=ax, label=f"{team} shots")
    else:
        # Use fixed size if xG not available
        pitch.scatter(team_shots.x, team_shots.y, s=100,
                    color=color, edgecolors='black', linewidth=1, alpha=0.7, ax=ax, label=f"{team} shots")
    
    # Annotate goals if outcome data is available
    if 'outcome_name' in shots.columns:
        goals = team_shots[team_shots['outcome_name'] == 'Goal']
        for _, goal in goals.iterrows():
            pitch.annotate(text=f"{goal['player_name']}", xy=(goal.x, goal.y), 
                        c='white', va='center', ha='center', size=8, ax=ax)

# Add legend and title
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.03), ncol=2)
ax.set_title(f"Champions League Final 2019: {home_team} vs {away_team}\nShot Map (size = xG)", fontsize=16)

# Show the plot
plt.tight_layout()
plt.show()