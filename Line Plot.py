

from matplotlib import pyplot as plt
import numpy as np
# create sample data
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,8,27,64,125,216,343,532,729,1000]
y2 = [1000,729,532,343,216,125,64,27,8,1,0]


# create a blank figure
fig = plt.figure()

x=np.linspace(2*-3.14,2*3.14,100)

y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure()

#plot onto the blank figure
plt.plot(x,y2, color="tab:green")
plt.plot(x,y1,linestyle="--",color="tab:purple")

plt.xlim([-6.28,6.28])
plt.ylim([-1.5,1.5])
plt.legend(["sin(x)","cos(x)"], loc="upper right")
plt.xlabel("x")
plt.ylabel("$f(x)$")



plt.show()