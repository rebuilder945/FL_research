import math
nums=eval(input())
n=sum(nums)/len(nums)
if n-math.floor(n)>0:
    print(n);
else:
    n=("%.2f"%n)
    print(n)

