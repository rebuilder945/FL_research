a=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
if (n+1)<=len(a):
    for x in range(m):
        a.append(a[n])
print(a)
