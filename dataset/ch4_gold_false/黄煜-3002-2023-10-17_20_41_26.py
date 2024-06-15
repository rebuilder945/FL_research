import math
list=eval(input())
a=sum(list)/len(list)
b=a-int(a)
if b==0:
    print("%d"%a)
else :
    print("%.2f"%a)
