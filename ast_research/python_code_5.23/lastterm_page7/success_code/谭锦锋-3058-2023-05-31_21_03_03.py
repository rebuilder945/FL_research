g = {}
a = input()
while a!='q':
    if a in g:
        g[a] += 1
    else:
        g[a] = 1
b = 0
for a in g.values():
    if a > b:
        b = a
        break
for a in g.keys():
    if g[a] == b:
        print("{}{}".format(a,b))
        break

