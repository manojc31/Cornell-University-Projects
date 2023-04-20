import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5980 (Decision Framing and Analytics)\Final Project\FilteredAmesHousing.csv')

x = data['SalePrice'].values
y = data['Gr Liv Area'].values
y2 = data['Year Built'].values
y3 = data['Lot Area'].values
y4 = data['Bedroom AbvGr'].values

fig, ax = plt.subplots(2,2, figsize=(12,10))
fig.tight_layout(pad=4.0)
ax[0,0].scatter(x,y,s=2, color='red')

ax[0,0].set_title("Sales Price vs Living Area Space")
ax[0,0].set_xlabel("Sales Price")
ax[0,0].set_ylabel("Living Area Space")

ax[0,1].scatter(x,y2,s=2, color='red')

ax[0,1].set_title("Sales Price vs Year Built")
ax[0,1].set_xlabel("Sales Price")
ax[0,1].set_ylabel("Year Built")


ax[1,0].scatter(x,y3,s=2, color='red')

ax[1,0].set_title("Sales Price vs Lot Area")
ax[1,0].set_xlabel("Sales Price")
ax[1,0].set_ylabel("Lot Area")

ax[1,1].scatter(y4,x,s=2,color='red')

ax[1,1].set_title("Sales Price vs Bedrooms")
ax[1,1].set_xlabel("Bedrooms")
ax[1,1].set_ylabel("Sales Price")

plt.show()

"""
ax[2].scatter(x,y,s=2)

ax[2].set_title("Sales Price vs Year Built")
ax[2].set_xlabel("Sales Price")
ax[2].set_ylabel("Year Built")

plt.show()
"""