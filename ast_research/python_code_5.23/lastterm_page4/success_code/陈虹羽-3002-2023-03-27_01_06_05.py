a=eval(input())
b=len(a)
c=sum(a)
d=c/b
e=c%b
if e==0:
    print("%d"%(d))
else:
    print("%.2f"%(d))

