a = list(map(int,input().split(",")))
n,m = eval(input())

if n>=0 and n<len(a):
    b = a[n:n+1]*m
    print(a+b)
elif n<0 and n>=(-1*len(a)):
    b = a[n:n-1]*m
    print(a+b)
else:
    print("error")

