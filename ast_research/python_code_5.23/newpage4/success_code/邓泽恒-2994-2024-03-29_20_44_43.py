a=eval(input())
a=list(a)
n,m=eval(input())
if n>len(a):
    print('error')
else:
    b=[a[n]]*m
    c=a+b
    print(c)
