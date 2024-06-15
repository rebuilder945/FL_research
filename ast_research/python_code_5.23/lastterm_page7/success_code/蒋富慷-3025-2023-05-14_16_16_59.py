a = input().split( )
b = {}
for i in a:
    b[i] = b.get(i,0)+1
c = list(b.values())
d = max(c)
for x in b:
    if b[x] != d:
        b.pop(x)
g = []
for e,f in b.items():
    g.append([e,f])
g.sort(key=lambda x:x[0])
for h in g:
    j,k = h
    print('%s %d'%(j,k))
