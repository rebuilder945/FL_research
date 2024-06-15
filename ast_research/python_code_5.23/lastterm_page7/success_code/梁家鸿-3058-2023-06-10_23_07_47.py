a = ""
b = {}
while (a != "q"):
    a = input()
    if b.get(a) == None:
        b[a] =  1
    else:
        b[a] = b[a] + 1
c = list(b.values())
d = max(c)
e = list(b.keys())[c.index(d)]
print(str(e) + ' ' + str(d))
