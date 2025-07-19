from mplsoccer import Sbopen
import pandas as pd

# Initialize the parser
parser = Sbopen()

# Load matches for Champions League 2018/2019
competition_id = 16  # Champions League
season_id = 4  # 2018/2019 season
df_matches = parser.match(competition_id=competition_id, season_id=season_id)

# Display match information
print(f"Champions League 2018/2019 matches:")
print(f"Total matches: {len(df_matches)}")
print("\nFirst 5 matches:")
# Show home team, away team, and match date for the first 5 matches
match_info = df_matches[['home_team_name', 'away_team_name', 'match_date']]
print(match_info.head())

# To load event data for a specific match, you would use:
# match_id = df_matches.iloc[0]['match_id']  # First match in the list
# df_events, related_events, freeze_frame, tactics = parser.event(match_id)