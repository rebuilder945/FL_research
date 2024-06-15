a=list(map(int,input().split(',')))
n,m=eval(input())
d=[]
if (n+1)<=len(a):
    for x in range(m):
        d.appenf(a[n])
    a=a+d
    print(a)
else:
    print('error')
