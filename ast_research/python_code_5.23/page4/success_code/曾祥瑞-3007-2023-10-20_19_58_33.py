a=eval(input())
n,m=eval(input())
if n in a and m in a:
    if n<=m:
        del a[n:m]
        print(a)
else:
    print("error")
