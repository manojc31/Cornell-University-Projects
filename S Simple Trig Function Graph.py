import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-1.5, 1.5, 1000)
y = np.linspace(-1.5, 1.5, 1000)

X, Y = np.meshgrid(x, y)
Z = np.sqrt((np.sin(X)**2 + np.cos(Y)**2))

fig = plt.figure(figsize=(10,8))
ax = fig.gca(projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('$Z=sin(x)^2 + sin(y)^2$')

ax.set_title('S simple Trig Function')
fig.colorbar(surf, shrink=0.5, aspect=10, label = '$Z=sin(x)^2 + sin(y)^2$')

plt.show()
plt.savefig('surface.png')