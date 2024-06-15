a=input()
p=input()
p=list(p.split(' '))
n=int(p[0])
m=int(p[1])
b=a.split(' ')
c=b[n]
d=b[m]
b.remove(c)
b.insert(m-1,c)
b.remove(d)
b.insert(n,d)
print(b)
