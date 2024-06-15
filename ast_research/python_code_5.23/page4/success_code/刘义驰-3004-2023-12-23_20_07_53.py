n = int(input())
L = []
for i in range(1, n + 1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        L.append(i)
print(L)

