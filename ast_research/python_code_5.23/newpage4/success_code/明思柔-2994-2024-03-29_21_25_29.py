a=list(eval(input()))
n,m=eval(input())
if n>=len(a):
    print('error')
else:
    c=[a[n]]*m
    a=a+c
    print(a)
