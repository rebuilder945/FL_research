a=eval(input())
n,m=eval(input())
d=len(a)
if n<d and m<d and n<=m:
    b=a[0:n+1]
    c=a[-1:m]
    d=b+c
    print(d)
else:
    print("error")
