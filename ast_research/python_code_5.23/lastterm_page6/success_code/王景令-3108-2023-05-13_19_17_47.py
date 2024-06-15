a = eval(input())
c = {}
a1 = ''.join(a)
a1.lower()
for i in a1:
    c[i] = c.get(i,0) + 1


b = c.items()
b.sort(key = lambda x : x[0])

for i in b:
    print(i[0],i[1],sep=',')
