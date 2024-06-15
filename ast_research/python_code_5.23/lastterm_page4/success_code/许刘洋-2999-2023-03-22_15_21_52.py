def change(y,m,n):
    y[m],y[n]=y[n],y[m]
    print(y)
y=input().split()
m,n=list(map(int,input().strip().split()))
change(y,m,n)
