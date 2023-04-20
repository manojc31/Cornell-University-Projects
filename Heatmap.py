
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Read in the data
heatwave = pd.read_csv(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5081 (Visualizing Data)\Python Code\heatwave.csv')

searches = heatwave.columns.values
data = heatwave[searches[1:]].values
data = data.transpose()
dates = heatwave[searches[0]]

fig = plt.figure(figsize=(14,6))
ax = fig.gca()

im = ax.imshow(data, cmap='RdYlBu_r')

plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
ax.set_ylim(-.5,8.5)

ax.set_title("Google trends summer, 2018", fontsize=14)

divider = make_axes_locatable(ax)
cax = divider.append_axes('bottom', size='12.5%', pad=1.2)
cbar = fig.colorbar(im, cax=cax, label='Search Interest Index',
                    orientation='horizontal')
cbar.set_label('Search Interest Index', labelpad=-50,
               rotation=0, fontsize=12)

fig.tight_layout()
plt.show()
plt.savefig('Part1_figure.png')
