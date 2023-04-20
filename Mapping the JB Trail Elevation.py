import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# make up some data
x = np.linspace(-250.0, 150.0, 30)
y = np.linspace(-30.0, 30.0, 30)

# make up the trail coordinates
jb_trail_x = x + np.random.rand(len(y)) * 40 - 30
jb_trail_y = y

# make a grid that is a combination of every x and every y
X, Y = np.meshgrid(x, y)

# the park elevation at each coordinate pair (x,y)
Z = abs(150 * np.cos(110 * X) ** 2 + 300 * np.sin(Y * 12)) + 7000

# elevation along the JR trail
jb_trail_elevation = np.zeros(30)
j = 0
for i in range(0, 30):
    jb_trail_elevation[j] = Z[i, i]
    j += 1

# x-axis variable for second subplot representing distance along trail
jb_trail_transect = np.linspace(0, 29, 30)

fig = plt.figure(figsize=(12, 6))

##############################################################
# Your code below - Do not modify the above code
##############################################################

fig, ((ax1), (ax2)) = plt.subplots(1, 2)
fig.tight_layout()

contour = ax1.contour(X, Y, Z, cmap='inferno_r')
ax1.clabel(contour, contour.levels, fontsize=8)

ax1.plot(jb_trail_x, jb_trail_y, color='black', linestyle='-.')

ax1.set_title('JB Trail Pups Peak Section')
ax1.set_xlim([-250,150])
ax1.set_xticks(np.linspace(-250,150,9))
ax1.set_ylim([-30,30])
ax1.plot()
#plt.show()



ax2.fill_between(jb_trail_transect, jb_trail_elevation, color='green')
ax2.set_xlim([0, 30])
ax2.set_xticks(np.linspace(0, 30, 7))
ax2.set_ylim([7000, 8000])
ax2.grid()
ax2.spines['left'].set_color('gray')
ax2.spines['top'].set_color('gray')
ax2.spines['right'].set_color('gray')
ax2.spines['bottom'].set_color('gray')
ax2.set_xlabel("Distance (mi)")
ax2.set_ylabel("Elev. (ft)")
ax2.set_title("Trail Profile at Pup's Peak")
ax2.annotate('Pup\'s Peak \nElevation 7,450 ft', xy =(10,7450), xytext=(12,7500), \
    arrowprops=dict(arrowstyle='simple', facecolor='black', edgecolor='none'))

ax2.plot()


plt.show()

##############################################################
# End of your code - Do not modify the following code
##############################################################

plt.savefig('Part1_figure.png', bbox_inches='tight')
