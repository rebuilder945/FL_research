   
a=list(eval(input()))
b=len(a)
c=sum(a)
d=c/b
a=3.14
if d%1==0:
    print(int(d))
elif d%1!=0:
    print("%.2f"%(d))
