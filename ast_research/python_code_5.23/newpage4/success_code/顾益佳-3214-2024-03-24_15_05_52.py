s = eval(input())
m = list (s)
j = 0
for x in m :
    if x == 0:
        j += 1
        m.remove(0)
    else:
        continue
for y in range(j):
    m.append(0)
print(m)

