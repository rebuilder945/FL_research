from calendar import c


n=eval(input())
m=n
a=2
b=3
c=1
d=2
e=a/1+b/2
while n-2>0:
    e+=(a+b)/(c+d)
    a,b=b,a+b
    c,d=d,c+d
    n-=1
if m==0:
    print(0)
elif m==1:
    print("%.4f"%a)
elif m==2:
    print("%.4f"%(a/1+b/2))
elif m>=3:
    print("%.4f"%e)
