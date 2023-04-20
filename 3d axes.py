import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.rand(200)
y = np.random.rand(200)
z = np.random.rand(200)

fig = plt.figure(figsize=(10,8))
ax = fig.gca(projection='3d')

ax.scatter(x,y,z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_title('A random distribution')
plt.show()
plt.savefig('Part_figure.png')