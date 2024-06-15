s = input()
m = eval(s)
mcopy1 = m.copy()
a = 0
y = 0
for x in m:
    if x == 0:
        a += 1
        mcopy1.remove(0)
    else:
        continue

while y < a:
    mcopy1.append(0)
    y += 1
print(mcopy1)
