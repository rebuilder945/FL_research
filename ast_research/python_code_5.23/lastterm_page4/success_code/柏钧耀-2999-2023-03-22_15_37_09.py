a=input()
b=a.split()
c=a.copy()
m=input()
d=m.split()
c[d[0]]=a[d[1]]
c[d[1]]=a[d[0]]

print(c)


