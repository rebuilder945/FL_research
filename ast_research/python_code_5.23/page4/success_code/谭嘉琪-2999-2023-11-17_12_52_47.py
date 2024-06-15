a=input().split()
n,m=map(int,input().split())
b=a[n]
c=a[m]
a.remove(b)
a.remove(c)
a.insert(n,c)
a.insert(m,b)
print(a)

