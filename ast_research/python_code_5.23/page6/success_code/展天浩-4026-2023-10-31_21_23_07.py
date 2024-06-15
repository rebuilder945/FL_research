n=int(input())
n1=n
a=1
b=2
c=2
d=3
e=0
while n-2>0:
    e+=(c+d)/(a+b)
    n-=1
if n1==1:
    print("%.4f"%(b))
elif n1==2:
    print("%.4f"%(d/b+b))
elif n1>=3:
    print("%.4f"%(e+b+d/b))
