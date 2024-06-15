a = input().split()
m,n =(input()).split()
m1 = int(m)
n2 = int(n)
d = a.copy()
i=m1-1
o=n2-1
a[i]=a[o]
a[o]=d[i]
print(a)






