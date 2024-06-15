a=eval(input())
b=len(a)
c=sum(a)/b
e=float(0)
d=c-int(c)
if d==0:
    print("%d"%(c))
elif d>0:
    print("%.2f"%(c))
