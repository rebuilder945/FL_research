a = input()
b = {}
c = []
for i in a :
    if i not in b:
        b[i] = 0
    else:
        b[i] += 1
for k,v in b.items() :
    if v == 0:
        c.append(k)
print(c[0])


