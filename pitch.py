import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch


# Draw pitch new axis
# pitch = Pitch()
# # Spesifying figure size (width, height) in inches
# fig, ax = pitch.draw(figsize=(8, 4))
# plt.show()

# Draw on an existing axis
# fig, axs = plt.subplots(nrows=1, ncols=2)
# pitch = Pitch()
# pie = axs[0].pie(x=[5,15])
# pitch.draw(ax=axs[1])
# plt.show()


# Supported data providers
pitch= Pitch(pitch_type='tracab', pitch_length=105, pitch_width=68, axis=True, label=True)
fig, ax = pitch.draw()
plt.show()

