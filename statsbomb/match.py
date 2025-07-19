from mplsoccer import Sbopen
import pandas as pd

# The first thing we have to do is open the data. We use a parser SBopen available in mplsoccer.
parser = Sbopen()
df_match = parser.match(competition_id=72, season_id=30)  # Example competition_id and season_id

# Display basic match information
print(f"Total matches: {len(df_match)}")

# Show match details
print("\nMatch Details:")
match_info = df_match[['match_date', 'home_team_name', 'away_team_name', 'home_score', 'away_score', 'away_team_managers_nickname']]
print(match_info.head(10))

# Display match with highest score
df_match['total_goals'] = df_match['home_score'] + df_match['away_score']
highest_scoring = df_match.loc[df_match['total_goals'].idxmax()]
print(f"\nHighest scoring match: {highest_scoring['home_team_name']} {highest_scoring['home_score']} - {highest_scoring['away_score']} {highest_scoring['away_team_name']}")

# structure of data
print("\nDataFrame Structure:")
df_match.info()