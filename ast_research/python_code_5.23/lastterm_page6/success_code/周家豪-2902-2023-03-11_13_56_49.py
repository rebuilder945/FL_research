def sum(n):
    a=2
    b=1
    c=int()
    sum=0
    for i in range(1,n+1):
        sum+=a/b
        c=a
        a=a+b
        b=c
    print("%.4f"%(sum))

n=int(input())
sum(n)
