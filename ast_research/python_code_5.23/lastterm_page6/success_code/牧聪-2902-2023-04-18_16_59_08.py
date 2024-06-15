a,b=2,3
c,d=1,2
n=int(input())
num=[2,1.5]
if n==1:
    print(2.000)
elif n==2:
    print(3.500)
else:
    for x in range(2,n+1):
        a,b=b,a+b
        c,d=d,c+d
        n=b/d
        print(b,d)
        num.append(n)
    SUM=sum(num)
    print("%.4f"%SUM)
        

