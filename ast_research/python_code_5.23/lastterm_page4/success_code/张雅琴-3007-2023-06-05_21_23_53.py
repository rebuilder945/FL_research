a=eval(input())
n,m=eval(input())
if n>=len(a) or m>=len(a):
    print("error")
elif n>=m:
    print("error")
else:
    print(a[0:n]+a[m:])
