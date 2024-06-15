a = eval(input())
m,n = eval(input())
if m < n:
    del a[m:n+1]
    print(a)
else:
    print("error")
