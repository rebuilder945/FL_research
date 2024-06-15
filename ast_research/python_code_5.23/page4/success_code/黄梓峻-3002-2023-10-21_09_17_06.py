import math
nums=eval(input())
n=sum(nums)/len(nums)
if n-math.floor(n)>0:
    n=("%.2f"%n)
    print(n);
else:
    print(n)

