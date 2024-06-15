a=list(input().split())
n,m=input().split()
n=int(n)
m=int(m)
c=a[n]
d=a[m] 
a.remove(c)
a.insert(m-1,c)
a.remove(d)
a.insert(n,d)
print(a)




