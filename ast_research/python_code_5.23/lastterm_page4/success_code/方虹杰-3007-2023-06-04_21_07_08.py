a=eval(input())
n,m=eval(input())
if 0<=n<m<len(a) or -len(a)<=n<m<=-1:
    del a[n:m]
    print(a)
else:
    print("error")

