import math
lst=eval(input())
a=sum(lst)/len(lst)
b=math.modf(a)
if b[0]==0:
    print("%d"%a)
else:
    print("%.2f"%a)
