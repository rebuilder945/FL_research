from math import sqrt
ax,ay=eval(input())
bx,by=eval(input())
dx=ax-bx
dy=ay-by
dstc=sqrt(abs(dx*dx-dy*dy))
print("%.2f"%(dstc))
