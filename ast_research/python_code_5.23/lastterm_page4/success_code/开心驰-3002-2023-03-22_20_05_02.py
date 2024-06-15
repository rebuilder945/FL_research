a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if d%1==0:
    print("%.d"%(d))
else:
    print("%.2f"%(d))
