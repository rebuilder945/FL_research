import math
a=eval(input())
sum=0
for i in range(0,len(a)):
    sum+=a[i]
    b=sum/len(a)
    c=math.modf(b)
    if c[0]==0:
        print("%d"%b)
    else:
        print("%.2f"%b)
