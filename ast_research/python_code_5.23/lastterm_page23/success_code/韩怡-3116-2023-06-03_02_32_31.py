x1,y1=eval(input())
x2,y2=eval(input())
d=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
import math
p=math.sqrt(d)
print("%.2f"%(p))
