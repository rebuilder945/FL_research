n=input().split(' ')
g={}
c=[]
for i in n:
    g[i]=n.count(i)
b=max(g.values())
for i in g:
    if g[i]==b:
        c.append(i)
    else:
        pass
c.sort()
for i in c:
    print('%s %s'%(i,b))
