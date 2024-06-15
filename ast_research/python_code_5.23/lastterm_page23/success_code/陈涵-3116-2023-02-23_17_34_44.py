import math
from math import sqrt
xa,ya=map(int,input().split(','))
xb,yb=map(int,input().split(','))
d =sqrt((xa-xb)*(xa-xb)+(ya-yb)*(ya-yb))
print("%.2f"%(d))
