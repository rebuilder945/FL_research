import math
xa,ya = map(int,input().split(","))
xb,yb = map(int,input().split(","))
dist = math.sqrt(1.0*(xa-xb)*(xa-xb)+1.0*(ya-yb)*(ya-yb))
print("%.2f"%(dist))

