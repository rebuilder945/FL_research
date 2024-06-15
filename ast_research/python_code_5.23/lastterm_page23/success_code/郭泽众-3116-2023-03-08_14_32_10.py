from math import sqrt
a1,a2=eval(input())
b1,b2=eval(input())
distance="%.2f"%float(sqrt((a1-b1)**2+(a2-b2)**2))
print(distance)
