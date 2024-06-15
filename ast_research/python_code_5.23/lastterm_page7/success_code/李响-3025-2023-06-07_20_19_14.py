a = input().split()
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
for i in sorted(b.keys(),reverse=False) :
 if b[i] == max(b.values()):
    print(i,b[i])

