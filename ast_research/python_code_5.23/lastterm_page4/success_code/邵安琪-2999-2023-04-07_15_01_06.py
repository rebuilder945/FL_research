def qqq(y,n,m):
    y[n],y[m]=y[m],y[n]
    print(y)
a = input()
n,m=list(map(int,input().strip().split()))
y = a.split()
qqq(y,n,m)
