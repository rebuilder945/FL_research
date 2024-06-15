a=list(eval(input()))
n,m=eval(input())
if n in range(len(a)):
    b=[a[n]]*m
    a.extend(b)
    print(a)
else:
    print('error')
