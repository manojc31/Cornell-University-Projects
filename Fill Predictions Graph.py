import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,101)
y1 = x**2
y2 = (x**2)/ 2
mean = (y1+y2)/ 2

fig = plt.figure(figsize=(8,6))
ax = fig.gca()

ax.fill_between(x, y1, y2, color='b', alpha=.4)

ax.plot(x,y1, color='b', linestyle='--', alpha = .8)
ax.plot(x, mean, color='b')
ax.plot(x, y2, color='b', linestyle='--', alpha=.8)

ax.set_xlabel('x data (units)')
ax.set_ylabel('y data (units)')
ax.set_ylim([0, 10000])
ax.set_xlim([0,100])
ax.legend(['Bounds', 'Mean'])
ax.set_title('Fill between example')

plt.show()
plt.savefig('Part1_figure.png')