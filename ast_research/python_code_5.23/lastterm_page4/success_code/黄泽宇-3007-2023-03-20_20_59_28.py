a=list(eval(input()))
n,m=eval(input())
p=len(a)
if n>p or m >p:
    print('error')
else:
    del a[n:m]
    print(a)
