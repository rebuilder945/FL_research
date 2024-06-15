a=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
d=[]
if (n+1)<=len(a):
    for x in range(m):
        d.append(a[n])
    a=a+d
    print(a)
else:
    print('error')
