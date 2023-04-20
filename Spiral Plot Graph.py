import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

z = np.linspace(0, 31.4, 1000)
x = np.sin(z)
y = np.cos(z)

fig = plt.figure(figsize=(10,8))
ax = fig.gca(projection='3d')

ax.plot3D(x, y, z)

ax.set_xlabel('$sin(z)$')
ax.set_ylabel('$cos(z)$')
ax.set_zlabel('z')

ax.set_title('A Spiral')
plt.show()
plt.savefig('Part2_figure.png')
