a=eval(input())
n,m=eval(input())
if n-1<=len(a) and m-1<=len(a) and n<m:
    del a[n:m]
else:
    print("error")
