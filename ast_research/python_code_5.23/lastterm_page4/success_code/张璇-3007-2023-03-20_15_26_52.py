a=eval(input())
n,m=eval(input())
if n<=m:
    del a[n:m]
    print(a)
elif n>m:
    print("error")
