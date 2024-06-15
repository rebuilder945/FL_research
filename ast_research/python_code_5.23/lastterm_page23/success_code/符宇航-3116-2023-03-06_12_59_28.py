import math 
x11,y11 = input().split(",")
x22,y22 = input().split(",")
x1 =float(x11)
y1 =float(y11)
x2 =float(x22)
y2 =float(y22)
d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("%.2f"%(d))
