a=eval(input())
n,m=eval(input())
if m>=len(a)-1:
    print("error")
else:
    if m>=n:
        del a[n:m]
        print(a)
    else:
        del a[m:n]
        print(a)
