a=list(eval(input()))
n,m=eval(input())
if n>len(a):
    print('error')
else:
    a+=[a[n]]*m
    print(a)
