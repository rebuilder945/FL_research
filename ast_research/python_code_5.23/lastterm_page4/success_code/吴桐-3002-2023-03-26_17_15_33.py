import math
li=eval(input())
pj=sum(li)/len(li)
b=math.modf(pj)
if b[0]==0:
    print("%.d"%pj)
else:
    print("%.2f"%pj)
