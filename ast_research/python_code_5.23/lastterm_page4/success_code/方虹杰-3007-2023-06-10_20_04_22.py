a=eval(input())
n,m=eval(input())
if n>=len(a) or m>=len(a):
    print("error")
else:
    del a[n:m]
    print(a)

