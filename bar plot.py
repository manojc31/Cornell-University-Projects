# import the required modules
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
width = 0.35
x_loc = np.array([0,1,2]) * (width*4)

child_survival_rate = np.array([0.916666667,0.913043478,0.347368421])
adult_survival_rate = np.array([0.648648649,0.414012739,0.221354167])
elderly_survival_rate = np.array([0.263157895,0.25,0.125])

fig = plt.figure()

plt.bar(x_loc, child_survival_rate, width, color = "tab:red")
plt.bar(x_loc + width, adult_survival_rate,width,color="tab:cyan")
plt.bar(x_loc + 2*width, elderly_survival_rate, width, color = "tab:purple")

plt.legend(["Child", "Adult", "Elderly"], loc= "upper right")
plt.xticks(x_loc + width, labels = ["First", "Second", "Third"])

plt.ylabel("Survival Rate")
plt.xlabel("Passenger Class")
plt.ylim([0,1])
plt.title("Titanic Survival Rates")

plt.show()