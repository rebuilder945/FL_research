a=list(map(int,input().split(',')))
n,m=map(int,input().split(','))
if (n+1)<=len(a):
    a.append(a[n]*m)
print(a)
