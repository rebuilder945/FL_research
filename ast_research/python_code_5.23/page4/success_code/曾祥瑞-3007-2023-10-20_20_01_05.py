a=eval(input())
n,m=eval(input())
if n in a or m in a:
    if n<=m:
        del a[n:m]
        print(a)
    else:
        del a[n:m:-1]
else:
    print("error")
