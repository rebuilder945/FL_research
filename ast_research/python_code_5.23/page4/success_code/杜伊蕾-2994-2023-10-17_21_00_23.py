a=list(map(int,input().split(',')))
n,m=eval(input())
d=[]
if n<=len(a):
    for x in range(m):
        d.append(a[n])
    a=a+d
    print(a)
else:
    print('error')
