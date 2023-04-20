import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3.14, 100)
cars = np.sin(x)**2
trucks = np.sin(x)
motorcycles = np.cos(x)**2

fig = plt.figure()
ax = fig.gca()

ax.fill_between(x, cars+trucks+motorcycles, cars+trucks, color='C0')
ax.fill_between(x, cars+trucks, cars, color='C1')
ax.fill_between(x, cars, np.zeros(len(x)), color='C2')

ax.set_xlim([0,3.14])
ax.set_xticks(np.linspace(0,3.14, 25))
ax.set_xticklabels(np.arange(0,25))
ax.set_ylim([0, 2.25])
ax.set_ylabel('Total highway traffic ($10^3$ vehicles)')
ax.set_xlabel('Hour of the day')
ax.legend(['motorcycles', 'trucks', 'cars'])
ax.set_title('Highway Traffic Breakdown')

plt.show()
plt.savefig('Part2_figure.png')
