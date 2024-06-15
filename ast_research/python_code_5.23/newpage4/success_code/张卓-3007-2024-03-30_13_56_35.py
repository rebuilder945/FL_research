a=list(eval(input()))
n,m=eval(input())
if n>m or n < 0 or m>=len(a):
    print("error")
else:
    b=a[0:n+1]
    c=a[m+1:-1]
    d=b+c
    print(d)
