import math

s1 = input()
s2 = input()
s1 = s1.split(",")
s2 = s2.split(",")
x1= float(s1[0])
y1 = float(s1[1])
x2= float(s2[0])
y2 = float(s2[1])
v = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print("%.2f" % v)
