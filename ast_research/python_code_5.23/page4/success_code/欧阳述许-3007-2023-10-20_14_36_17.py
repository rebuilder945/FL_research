a,n,m=eval(input())
if n<=len(a):
    for x in range(n,m):
        if n>len(a)-1 or m>len(a)-1:
            print("error")
else:
    if n<=m:
        del a[n,m]
    else:
        n,m=m,n
        del a[n+1,m+1]
    print(a)

