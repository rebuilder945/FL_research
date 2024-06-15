a = input()
n,m = input()
if n and m in a:
    if n<m:
        del a[n,m]
        print(a)
    else:
        del a[m+1,n+1]
        print(a)
else:
    print("error")
