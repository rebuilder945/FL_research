a=eval(input())
n,m=eval(input())
if n<=m:
    del a[n:m:1]
    print(a)
else:
    print("error")
