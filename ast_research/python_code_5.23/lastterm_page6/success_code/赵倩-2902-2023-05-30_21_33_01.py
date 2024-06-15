a=eval(input())
b1=2
c1=1
l1=2
b2=3
c2=2
l2=3.5
if a==2:
    print("%.4f"%l2)
elif a>2:
    for i in range(a-2):
        n=b1+b2
        m=c1+c2
        l2+=n/m
        b1,b2=b2,n
        c1,c2=c2,m
    print("%.4f"%l2)
elif a==1:
    print("%.4f"%l1)


