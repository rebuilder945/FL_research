import math
list=eval(input())
a=sum(list)/len(list)
if a/1==0:
    b=math.modf(a)
    print(b)
else:
    print("%.2f"%a)
