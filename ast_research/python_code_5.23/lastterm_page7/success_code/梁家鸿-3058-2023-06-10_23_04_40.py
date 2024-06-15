a = input() or "q"
b = {}
while (a != "q"):
    if b.get(a) != None:
        b[a] =  1
    else:
        b[a] += 1
c = list(b.values())
d = max(c)
e = list(b.keys())[c.index(d)]
print(str(e) + ' ' + str(d))
