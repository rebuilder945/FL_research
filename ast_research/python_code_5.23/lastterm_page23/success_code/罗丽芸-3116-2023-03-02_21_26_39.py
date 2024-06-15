x1,y1=input().split(",")
x2,y2=input().split(",")
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
d=(x1-x2)*(x1-x2)+(y1-y2)+(y1-y2)
import math
print("%.2f"%(math.sqrt(d)))
