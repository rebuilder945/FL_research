a=list(eval(input()))
n,m=eval(input())
if n>m or n < 0 or m>=len(a):
    print("error")
else:
    del a[n:m]
    print(a)
