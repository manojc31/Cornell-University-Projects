from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import numpy as np
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
stress_strain = np.loadtxt(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5081 (Visualizing Data)\Python Code\stress_strain.csv', delimiter=',')


#plate failure project
time = np.linspace(0,100, 101)
displacement = np.concatenate([np.random.rand(70), np.random.rand(31)+3])
x = np.linspace(-10.0, 10.0, 1000)
y = np.linspace(-10.0, 10.0, 1000)

ave_displacement = moving_average(displacement, n=4)
ave_displacement = np.concatenate([ave_displacement[0:3], ave_displacement])

stress_true = stress_strain[:,0]
strain_true = stress_strain[:,1]
stress_est = stress_strain[:,2]
strain_est = stress_strain[:,3]
stress_est_max = 1.15*stress_est
stress_est_min = .9*stress_est

# grid for cross section
X, Y = np.meshgrid(x, y)
Z = abs(X + Y)

# create a figure object
fig = plt.figure(figsize=(12,8))

##############################################################
# Your code below - Do not modify the above code
##############################################################
gspec = fig.add_gridspec(ncols=2, nrows=2)
fig.subplots_adjust(hspace=.5, wspace=.25)

#################################PLOT 1#############################
ax=fig.add_subplot(gspec[0,:2])
ax.scatter(time,displacement,color='red')
ax.plot(time,ave_displacement,linestyle='--',color='blue')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (μm)')
ax.legend(["Observation","Rolling Mean"],loc='upper left')
ax.set_xlim([0,100])
ax.set_ylim([0,4])

ax.annotate('Fracture occured \nafter 45 seconds', xy=(70,2), xytext=(50,3), \
            arrowprops=dict(arrowstyle='simple', facecolor='black', edgecolor='none'))

ax.set_title('Plate Fracture Test Results')

#################################PLOT 2#############################
ax2=fig.add_subplot(gspec[1,0:1])
ax2.plot(strain_est,stress_est,linestyle='--',color='green')
ax2.plot(strain_true,stress_true,color='green')
ax2.fill_between(strain_est,stress_est_max ,stress_est_min,color='green', alpha=.4)

ax2.set_xlabel('ε(kN/$cm^2$)')
ax2.set_ylabel('σ(kN)')
ax2.set_title('Stress Strain Relationship')
ax2.set_xlim([0,0.10])
ax2.set_ylim([0,550])
ax2.legend(["Estimated","Actual","95% conf"], loc='lower right')

#################################PLOT 3#############################
ax3=fig.add_subplot(gspec[1,1:2])

im = ax3.imshow(Z, cmap='inferno_r')

ax3.set_xlabel('x (cm)')
ax3.set_ylabel('y (cm)')
ax3.set_title('Plate Cross Section')
divider = make_axes_locatable(ax3)
cax = divider.append_axes('right',size='5%', pad=0.1)
cbar = fig.colorbar(im,cax=cax)
cbar.set_label('$\sigma (kN)$', labelpad=10,
rotation=90, fontsize=12)

plt.tight_layout()
plt.show()

##############################################################
# End of your code - Do not modify the following code
##############################################################

plt.savefig('Part2_figure.png', bbox_inches='tight')

