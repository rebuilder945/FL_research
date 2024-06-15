n=eval(input())
fz=1
fm=2
lst=[]
sum=0
for i in range(1,n+1):
    a=fz
    b=fm
    sum+=a/b
    lst.append("%s%s"%(a,b))
    fz=a+b
    fm=a
    print("%.4f"%sum)
