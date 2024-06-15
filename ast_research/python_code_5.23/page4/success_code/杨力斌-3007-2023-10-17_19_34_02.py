a = eval(input())
n,m = eval(input())
if m >= n:
    del a[n:m]
    print(a)
else:
    print("error")
