import math
a=eval(input())
b=sum(a)/len(a)
c=math.floor(b)
if b>c:
    print("%.2f"%(b))
else:
    print(c)

