import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen, VerticalPitch

parser = Sbopen()
df, related, freeze, tactics = parser.event(69301)
#get team names
team1, team2 = df.team_name.unique()
print(f"Visualizing shots from {team1} vs {team2}")

#A dataferame of shots
shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
print(f"Total shots in match: {len(shots)}")

pitch = Pitch(line_color='black')
fig, ax = pitch.draw(figsize=(10, 7))

#Size of the pitch in yards (!!!)
pitchLengthX = 120
pitchLengthY = 80

#Plot the shots by looping through them
for i, shot in shots.iterrows():
   #Get the information
    x= shot['x']
    y= shot['y']
    goal = shot['outcome_name'] == 'Goal'
    team_name = shot['team_name']
    #Set circle size
    circleSize = 2
    #Plot England
    if team_name == team1:
        color = 'blue'   
        if goal:
            shotCircle = plt.Circle((x, y), circleSize, color=color)
            plt.text(x+1, y-2, shot['player_name'])
        else:
            shotCircle = plt.Circle((x,y), circleSize, color=color)
            shotCircle.set_alpha(.2)
    else:
        if goal:
                color = 'red'
                shotCircle = plt.Circle((pitchLengthX-x, pitchLengthY-y), circleSize, color=color)
                plt.text(pitchLengthX-x+1, pitchLengthY-y-2, shot['player_name'])
        else:
                shotCircle = plt.Circle((pitchLengthX- x,pitchLengthY-y), circleSize, color=color)
                shotCircle.set_alpha(.2)
        #Add the circle to the plot
    ax.add_patch(shotCircle)

# Add the title
fig.suptitle("England (red) and Sweden (blue) shots", fontsize = 24)
fig.set_size_inches(10, 7)
plt.show()


