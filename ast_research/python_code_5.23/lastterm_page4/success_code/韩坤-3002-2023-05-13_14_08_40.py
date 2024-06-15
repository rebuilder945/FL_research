import math
a=eval(input())
b=sum(a)/len(a)
if b-math.floor(b)==0:
    print("%d"%(b))
else:
    print("%.2f"%(b))
