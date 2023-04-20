import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
######CODE WORKING########
# read in csv files
setosa_df = pd.read_csv(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5081 (Visualizing Data)\Python Code\setosa.csv')
setosa_sepal_length = setosa_df['sepal_length'].values
setosa_sepal_width = setosa_df['sepal_width'].values


versicolor_df = pd.read_csv(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5081 (Visualizing Data)\Python Code\versicolor.csv')
versicolor_sepal_length = versicolor_df['sepal_length'].values
versicolor_sepal_width = versicolor_df['sepal_width'].values

virginica_df = pd.read_csv(r'C:\Users\manoj\OneDrive\Documents\Cornell University\ENMGT 5081 (Visualizing Data)\Python Code\virginica.csv')
virginica_sepal_length = virginica_df['sepal_length'].values
virginica_sepal_width = virginica_df['sepal_width'].values

fig = plt.figure() # keep the figure name as "fig"

#Setosa
x = setosa_sepal_length
y = setosa_sepal_width

#Versicolor
x1 = versicolor_sepal_length
y1 = versicolor_sepal_width

#Virginica
x2 = virginica_sepal_length
y2 = virginica_sepal_width


plt.scatter(x,y, alpha = 0.8, color = "blue")
plt.scatter(x1,y1, alpha = 0.8, color = "orange")
plt.scatter(x2,y2, alpha = 0.8, color = "green")



plt.title("Iris Data Sepal Dimensions")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.xlim([4,8])
plt.ylim([1,5])
plt.legend(["Setosa","Versicolor","Virginica"],loc='upper right')

plt.show()
