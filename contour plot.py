import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# make up some data
x = np.linspace(-4.0, 4.0, 1000)
y = np.linspace(-4.0, 4.0, 1000)

# make a grid that is a combination of every x and every y
X, Y = np.meshgrid(x, y)
Z = np.sqrt(abs(X**3 + Y**3))

# set up the figure
fig = plt.figure(figsize=(8,8))
ax = fig.gca()

###############################################################
# Add code below
###############################################################

contour = ax.contour(X, Y, Z, cmap='inferno_r')
ax.clabel(contour, contour.levels, fontsize=8)

ax.set_xlabel('Horizontal Position (in)')
ax.set_ylabel('Vertical Position (in)')

ax.set_title('Onion Energy Field')
plt.show()
plt.savefig('Part3_figure.png')