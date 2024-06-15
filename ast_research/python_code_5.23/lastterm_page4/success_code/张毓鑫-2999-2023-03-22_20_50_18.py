a=input()
n,m=map(int,(input().split()))
a=a.split()
b=a[n]
a.insert(m,b)
c=a[m+1]
del a[m+1]
a.insert(n,c)
del a[n+1]
print(a)
