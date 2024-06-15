import math
a=eval(input())
b=sum(a)/len(a)
c=math.modf(b)
if c[0]==0:
    print("%d"%(b))
else:
    print("%.2f"%(b))
