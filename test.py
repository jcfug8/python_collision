import math

# y = 11
# x = 13
# y1 = 1
# y2 = 0
# x1 = 1
# x2 = 0
# radius = 10
#
# m = (y1 - y2) / (x1 - x2)
# b = y1 - m * x1
# temp_x = (y-b)/m
# print ("x", temp_x )
# print ("y", m * temp_x + b)
# print ((y-b)/m, m * (y-b)/m + b)
# temp_y = m * x + b
# print ("y", temp_y )
# print ("x", (temp_y - b)/m)
# print (((m * x + b) - b)/m , m * x + b)

a = 3
b = 7
c = 5
s = (a+b+c)/2
Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(Area)
