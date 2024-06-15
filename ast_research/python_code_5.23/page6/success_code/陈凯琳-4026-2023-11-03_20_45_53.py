n=int(input())
if n==1:
    print(2)
elif n==2:
    print(3.5)
else:
    a=[2,3]
    b=[1,2]
    lit=[]
    for i in range(n-2):
        c=a[-1]+a[-2]
        a.append(c)
    for i in range(n-2):
        d=b[-1]+b[-2]
        b.append(d)
    for i in range(len(a)):
        x=a[i]/b[i]
        lit.append(x)
    m=sum(lit)
    print("%.4f"%m)

