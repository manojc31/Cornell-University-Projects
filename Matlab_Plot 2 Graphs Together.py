from matplotlib import pyplot as plt

# create sample data
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,8,27,64,125,216,343,532,729,1000]
y2 = [1000,729,532,343,216,125,64,27,8,1,0]

# create a blank figure
fig = plt.figure(figsize=(6,4))

#plot onto the blank figure
plt.plot(x,y,label='y1', linestyle='--',color='green')
plt.plot(x,y2,label='y2',linestyle=':',color='purple')

#add x an y labels
plt.xlabel('x Data', fontsize=12)
plt.ylabel('y Data', fontsize=12)

#set axis labels
plt.xlim(0,10)
plt.ylim(0,1000)

#give the plot a title
plt.title('My first plot', fontsize=16)
plt.show()