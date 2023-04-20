from math import sin
a = 7
b = 0.1
x1 = 1
x2 = 1
x3 = 1
delta_x = 0.01

y = sin(x1) + (a*(sin(x2)**2)) + (b*(sin(x3)**4))

# delta_x1
y1 = sin(x1+delta_x) + (a*(sin(x2)**2)) + (b*(sin(x3)**4))

# delta_x2
y2 = sin(x1) + (a*(sin(x2+delta_x)**2)) + (b*(sin(x3)**4))

# delta_x3
y3 = sin(x1) + (a*(sin(x2)**2)) + (b*(sin(x3+delta_x)**4))

s1 = y1 / (x1+delta_x)
s2 = y2 / (x2+delta_x)
s3 = y3 / (x3+delta_x)

print("The value of delta y1 is ", y1)
print("The value of delta y2 is ", y2)
print("The value of delta y3 is ", y3)

print("The value of s1 is ", s1)
print("The value of s2 is ", s2)
print("The value of s3 is ", s3)
