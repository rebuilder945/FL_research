a=list(input())
b=len(a)
c=sum(a)
d=c/b
a=3.14
if d%1==0:
    print(d)
elif d%1!=0:
    print("%.2f"%(d))
