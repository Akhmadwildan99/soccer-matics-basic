#importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from mplsoccer import Pitch, Sbopen

parser = Sbopen()
df, related, freeze, tactics = parser.event(69301)
passes = df.loc[df['type_name']== 'Pass'].loc[df['sub_type_name'] != 'Throw-in'].set_index('id')

#drawing the pitch
#drawing pitch
pitch = Pitch(line_color = "black")
fig, ax = pitch.draw(figsize=(10, 7))
for i, thepass in passes.iterrows():
    #if pass made by Lucy Bronze
    if thepass['player_name'] == 'Lucy Bronze':
        #plotting the pass
       x = thepass['x']
       y = thepass['y']
       end_x = thepass['end_x'] - x
       end_y = thepass['end_y'] - y
       #plot circle
       pass_circle = plt.Circle((x,y), 2, color='blue')
       pass_circle.set_alpha(.2)
       ax.add_patch(pass_circle)
       #plot the arrow
       pass_arrow = plt.Arrow(x, y, end_x, end_y, width=3, color='blue')
       ax.add_patch(pass_arrow)

fig.suptitle("Lucy Bronze's passes against Sweden", fontsize=24)
fig.set_size_inches(10, 7)
plt.show()
