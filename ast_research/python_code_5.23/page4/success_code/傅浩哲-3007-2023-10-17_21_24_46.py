a=eval(input())
n,m=eval(input())
if n<m and 0<=n<=len(a) and 0<m<=len(a):
    for i in range(n,m):
        a[n:m]=[]
    print(a)
else:
    print('error')
