a = eval(input())
m,n = eval(input())
if m < n:
    del a[n:m:-1]
    print(a)
else:
    print("error")
