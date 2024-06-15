a=input()
b=input()
f=a.split(a)
g=b.split(b)
c=[]
for x in range(len(f)):
    d=[f[x],g[x]]
    c.append(d)
c.sort(key=lambda x:x[1])
print(c)
