
from math import sqrt

ax,ay=input().split(',')
bx,by=input().split(',')
julix=sqrt(((int(ax)-int(bx))**2)+((int(ay)-int(by))**2))
print("%.2f"%julix)
