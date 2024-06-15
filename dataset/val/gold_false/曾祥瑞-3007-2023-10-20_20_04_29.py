a=eval(input())
n,m=eval(input())
if n < len(a) or m < len(a):
    if n<=m:
        del a[n:m]
        print(a)
    else:
        del a[n:m:-1]
else:
    print("error")
