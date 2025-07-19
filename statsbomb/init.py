#importing SBopen class from mplsoccer to open the data
from mplsoccer import Sbopen
# The first thing we have to do is open the data. We use a parser SBopen available in mplsoccer.
parser = Sbopen()
df_competition = parser.competition()
#structure of data
df_competition.info()

# Display the competitions available
print("\nAvailable competitions:")
print(df_competition[["country_name", "competition_name", "season_name"]].head(10))

# Filter for Champions League competitions
print("\nChampions League seasons:")
cl_competitions = df_competition[df_competition["competition_name"] == "Champions League"]
print(cl_competitions[["competition_id", "season_id", "season_name"]])