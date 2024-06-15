a = input().split(' ')
b = {}
for x in a:
    if b.get(x) == None:
        b[x] = 1
    else:
        b[x] = b[x] + 1
c = list(b.values())
d = list(b.keys())
e = max(c)
f = []
for k , v in b.items():
    if v == e:
       f.append(k)
f.sort()
for y in f:
    print(y+' '+str(e))
