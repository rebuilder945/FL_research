a=eval(input())
n,m=map(int,input().split(","))
if n<=m:
    del a[n,m]
    print(a)
else:
    print("error")
