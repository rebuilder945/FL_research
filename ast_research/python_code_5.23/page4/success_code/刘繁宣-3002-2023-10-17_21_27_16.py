ls=eval(input())
a=sum(ls)/len(ls)
import math
if a==math.floor(a):
    print("%d"%a)
else:
    print("%.2f"%a)
