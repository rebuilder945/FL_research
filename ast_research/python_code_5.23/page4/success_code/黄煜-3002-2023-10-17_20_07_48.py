import math
list=eval(input())
a=sum(list)/len(list)
if a/1==0:
    print("%d"%a)
elif a/1!=0:
    print("%.2f"%a)
