a = eval(input())
n,m = eval(input())
if(n>m or n<0 or n>=len(a) or m<0 or m>=len(a)):
    print("error")
else:
    print(a[:n]+a[m:])

