nums=eval(input())
a=sum(nums)
b=len(nums)
c=a%b
d=a/b
if c==0:
    print("%d"%(d))
else:
    print("%.2f"%(d))
