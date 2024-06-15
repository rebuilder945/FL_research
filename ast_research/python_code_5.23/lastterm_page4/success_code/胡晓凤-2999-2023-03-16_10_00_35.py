def lst(y,m,n):
    y[m],y[n]=y[n],y[m]
    print(y)
lst=[input().split(" ")]
n,m=eval(input()).split(" ")
y=lst
lst(y,m,n)
