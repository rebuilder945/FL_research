a=input()
b=input()
f=a.split(',')
g=b.split(',')
c=[]
for x in range(len(f)):
    d=[f[x],g[x]]
    c.append(d)
c.sort(key=lambda x:x[1])
print(c)
