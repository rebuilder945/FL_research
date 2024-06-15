def Change(y,m,n):
    y[m],y[n]=y[m],y[n]
    print(y);
sums=input();
m,n = list(map(int,input().strip().split()))
y=sums.split();
Change(y,m,n);
