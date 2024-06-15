a=list(input().split(' '))
b,c=input().split(' ')
g=a.copy()
g.append("q")
e=int(b)
f=int(c)
for x in g[e:e+1]:
    m=x
for y in g[f:f+1]:
    n=y
a[e]=n
a[f]=m
print(a)
