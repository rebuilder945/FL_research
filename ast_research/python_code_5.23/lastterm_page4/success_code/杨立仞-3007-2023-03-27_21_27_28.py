a=eval(input())
n,m=eval((input()))
if n<=m:
    if m>(len(a)-1):
        print("error")
    else:
        del a[n:m]
        print(a)
else:
    print("error")
