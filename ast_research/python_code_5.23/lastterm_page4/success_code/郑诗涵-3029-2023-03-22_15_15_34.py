names = input().split(',')
f = eval(input())
m = list(names)
s = len(m)
k = ()
g = []
for i in range(s):
    k = (m[i],f[i])
    g.append(list(k))
print(g)
