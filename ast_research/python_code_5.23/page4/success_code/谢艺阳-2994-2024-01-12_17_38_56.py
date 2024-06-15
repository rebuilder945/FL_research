a=input().split(",")
a=list(map(int,a))
n,m=eval(input())
b=len(a)
if n>b or-n>=b:
    print("error")
else:
    c=[a[n]]
    d=c*m
    print(a+d)

