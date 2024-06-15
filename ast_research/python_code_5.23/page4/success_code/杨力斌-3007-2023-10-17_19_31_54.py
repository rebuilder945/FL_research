a = eval(input())
m,n = eval(input())
if m < n:
    del a[m:n]
    print(a)
else:
    print("error")
