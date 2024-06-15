n = input().split(',')
g = input().split(',')
g = [int(x) for x in g]
print(n,g)
gra = {}
for x in n:
    gra[x] = g[n.index(x)]
i = [list(x) for x in gra.items()]
i.sort(key=lambda x:x[1])
print(i)
