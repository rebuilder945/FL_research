nums=eval(input())
n=sum(nums)/len(nums)
if type(n)==int:
    print(n);
else:
    n=("%.2f"%n)
    print(n)

