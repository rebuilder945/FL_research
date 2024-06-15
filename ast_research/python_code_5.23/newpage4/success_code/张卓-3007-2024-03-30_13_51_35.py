a=list(eval(input()))
n,m=eval(input())
if n>m or n<=len(a) or n>=len(a) or m<=len(a) or m>=len(a):
    print("error")
else:
    b=a[0:n]
    c=a[m+1:-1]
    d=b+c
    print(d)
