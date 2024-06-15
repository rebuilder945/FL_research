a = input().split()
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
sorted(b.keys())
for i in b:
 if b[i] == max(b.values()):
    print(i,b[i])

