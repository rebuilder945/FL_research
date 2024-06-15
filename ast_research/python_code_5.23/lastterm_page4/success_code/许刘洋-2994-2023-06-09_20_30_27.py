a=list(eval(input()))
b=a[::]
n,m=eval(input())
if n>len(a):
    print('error')
else:
    c=a[n]*m
    b+=c
    print(b)
