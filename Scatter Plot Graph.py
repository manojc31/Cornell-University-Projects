import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(30)
z = np.random.normal(15,30,30)
y = x*4+z
size_vals = np.random.rand(30)*1000

plt.scatter(x,y,c=abs(z),edgecolor = "none", cmap="viridis", alpha=0.8, s=size_vals)

plt.title("A scatter plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.xlim([-3,33])
plt.ylim([-30,175])

plt.show()