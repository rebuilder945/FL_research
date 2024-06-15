a=eval(input())
n,m=eval(input())
if n < len(a)-1 or m < len(a)-1:
    if n<=m:
        del a[n:m]
        print(a)
    else:
        del a[n:m:-1]
else:
    print("error")
