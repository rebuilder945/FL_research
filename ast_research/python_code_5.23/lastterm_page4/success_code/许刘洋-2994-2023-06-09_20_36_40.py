a=list(eval(input()))
b=a[::]
n,m=eval(input())
if n>len(a):
    print('error')
else:
    b+=[a[n]]*m
    print(b)
