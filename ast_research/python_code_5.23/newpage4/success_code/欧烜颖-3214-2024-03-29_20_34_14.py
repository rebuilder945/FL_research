from re import A, S


s = input()
m = eval(s)
a = 0
y = 0
for x in m:
    if x == 0:
        a += 1
        m.remove(0)
    else:
        continue
while y <= a:
    m.append(0)
    y += 1
print(m)
