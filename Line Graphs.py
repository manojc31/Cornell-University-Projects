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
plt.ylim([0,110])






ax.set_yticklabels(['Very Low','Low','Moderate','High','Very High','Viral'])

plt.xlabel("Days from June 4th, 2018")
plt.ylabel("Search Interest Index")
plt.title("Google search interest during summer 2018")
plt.legend(["Fan","Barbecue","Swimsuit"],loc="lower left")
################################################################
# End of your code - Do not modify the rest of the code
################################################################
plt.show()
# save figure
plt.savefig('Part3_fig.png')