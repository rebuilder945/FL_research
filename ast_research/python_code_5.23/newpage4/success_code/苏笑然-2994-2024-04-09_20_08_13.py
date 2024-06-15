a=input().split(',')
n,m=eval(input())
n=n
l=len(a)
if l>=n:
    b=a.pop(n)
    c=[b]*m
    d=a+c
    print(d)
else:
    print('error')
