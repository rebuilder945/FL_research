n=int(input())
n1=n
a=1
b=2
c=2
d=3
e=c/1+d/2
while n-2>0:
    e+=(c+d)/(a+b)
    c,d=c,c+d
    a,b=b,a+b
    n-=1
if n1==0:
    print(0)
elif n1==1:
    print("%.4f"%(c))
elif n1==2:
    print("%.4f"%(c/1+d/2))
elif n1>=3:
    print("%.4f"%(e))
