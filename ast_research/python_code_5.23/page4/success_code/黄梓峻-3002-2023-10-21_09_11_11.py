nums=eval(input())
n=sum(nums)/len(nums)
if n-int(n)>0:
    print(n);
else:
    n=("%.2f"%n)
    print(n)

