a=list(eval(input()))
n,m=eval(input())
if  n<len(a)+1:
    b=[a[n]]*m
    print(b)
    a.extend(b)
    print(a)
else:
    print('error')
