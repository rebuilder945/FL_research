import math
a=eval(input())
b=sum(a)/len(a)
b1=math.modf(b)
if b1[0]==0:
    print("%d"%b)
else:
    print("%.2f"%b)


