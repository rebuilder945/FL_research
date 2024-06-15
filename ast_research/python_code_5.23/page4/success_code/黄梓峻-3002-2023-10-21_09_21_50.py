import math
nums=eval(input())
n=sum(nums)/len(nums)
if n-math.floor(n)>0:
    m=("%.2f"%n)
    print(m);
else:
    int(n)
    print(n)


