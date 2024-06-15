a = eval(input())
m,n = eval(input())
if m < n:
    del a[m:n+2]
    print(a)
else:
    print("error")
