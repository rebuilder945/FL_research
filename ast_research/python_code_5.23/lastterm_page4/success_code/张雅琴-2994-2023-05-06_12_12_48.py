a=list(eval(input()))
n,m=eval(input())
if n<len(a):
    b=[a[n]]*m
    c=a+b
    print(c)
else:
    print('error')
