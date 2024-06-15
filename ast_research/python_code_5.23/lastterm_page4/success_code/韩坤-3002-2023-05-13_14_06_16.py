import math
a=eval(input())
b=sum(a)/len(a)
if b-math.floor(b)==0:
    print(b)
else:
    print("%.2f"%(b))
