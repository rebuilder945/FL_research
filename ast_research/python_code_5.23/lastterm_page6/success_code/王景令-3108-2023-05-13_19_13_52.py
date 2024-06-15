a = eval(input())
c = {}
a1 = ''.join(a)
for i in a1:
    c[i] = c.get(i,0) + 1


b = c.items()
print(b)
for i in b:
    print(i[0],i[1],sep=',')
