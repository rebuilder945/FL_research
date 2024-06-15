a=input().split(',')
n,m=eval(input())
l=len(a)
if l>=n:
    b=a[n]
    c=[b]*m
    d=a+c
    print(d)
else:
    print('error')
