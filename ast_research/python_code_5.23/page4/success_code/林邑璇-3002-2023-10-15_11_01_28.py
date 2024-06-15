a=eval(input())
b=len(a)
c=sum(a)
d=c/b
if d%1==0:
    print("%d"%(d))
else:
    print("%.2f"%(d))
