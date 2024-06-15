a=input().split(',')
n,m=eval(input())
n=n-1
l=len(a)
if l>=n:
    b=a.pop(n)
    c=[b]*m
    d=a+c
    print(d)
else:
    print('error')
