def lst(y,m,n):
    y[m],y[n]=y[n],y[m]
    print(y)
lst=input()
m,n=list(map(int,input().strip().split()))
y=lst.split()
lst(y,m,n)
