a=eval(input())
n,m=eval(input())
if n>len(a)-1 or m>len(a)-1:
    print("error")
else:
    if n<=m:
        del a[n:m]
    else:
        print(a)
    print(a)
