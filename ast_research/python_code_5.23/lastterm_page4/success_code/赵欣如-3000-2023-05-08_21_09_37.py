ls1=eval(input())
a=sum(ls1)/len(ls1)
import math
b=math.floor(a)
if a-b==0:
    print("%.0f"%a)
if a-b!=0:
    print("%.2f"%a) 

