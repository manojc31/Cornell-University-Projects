# import the required modules
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Read in the data
heatwave = pd.read_csv(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5081 (Visualizing Data)\Python Code\heatwave.csv')

barbecue = heatwave['Barbecue'].values
fan = heatwave['Fan'].values
swimsuit = heatwave['Swimsuit'].values

days = np.arange(58)

fig = plt.figure() # Keep the figure name as "fig"

################################################################
# Your code here - Do not modify the above code
################################################################
plt.grid()
ax = plt.gca()
ax.plot(fan,color="tab:purple")
ax.plot(barbecue,linestyle="--",color="tab:orange")
ax.plot(swimsuit,linestyle=":",color="cyan")
plt.xlim([0,58])
plt.ylim([0,130])


ax.annotate('Barbecue and Swimsuit searches \npeaked on weekends', xy =(6,91), xytext=(2, 100), \
 arrowprops=dict(arrowstyle='simple', facecolor='k', edgecolor='none'))



ax.set_yticklabels(['Zero','Very Low','Low','Moderate','High','Very High','Viral'])
ax.set_yticks([10, 30, 50, 70, 90, 110], minor=True)

plt.xlabel("Days from June 4th, 2018")
plt.ylabel("Search Interest Index")
plt.title("Google search interest during summer 2018")
plt.legend(["Fan","Barbecue","Swimsuit"],loc="lower right")
################################################################
# End of your code - Do not modify the rest of the code
################################################################
plt.show()
# save figure
plt.savefig('heatwave_figure.png')