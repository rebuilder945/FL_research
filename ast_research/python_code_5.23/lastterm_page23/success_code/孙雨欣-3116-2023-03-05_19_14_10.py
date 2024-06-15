import math
x1,y1=map(int,input().split(','))
x2,y2=map(int,input().split(','))
L=((x2-x1)**2+(y2-y1)**2)**0.5
print(round(L,2))

