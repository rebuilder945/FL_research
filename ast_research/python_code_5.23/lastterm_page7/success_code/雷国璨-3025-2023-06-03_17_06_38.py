n=input().split(' ')
g={}
for i in n:
    g[i]=n.count(i)
b=max(g.values())
for i in g:
    if g[i]==b:
        print('%s %s'%(i,b))
    else:
        pass

