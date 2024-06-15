s = eval(input())
m = list (s)
i = 0
j = 0
for x in m :
    if x == 0:
        j += 1
        del m[i]
        i += 1
    else:
        i += 1
for y in range(j):
    m.append(0)

print(m)

