a=list(input().split())
n,m=map(int,input().split())
a.insert(n,a[m])
del a[m+1]
print(a)
