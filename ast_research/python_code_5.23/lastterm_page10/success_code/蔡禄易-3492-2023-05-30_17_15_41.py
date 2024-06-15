a = input().split()
b = []
for i in a:
    if i not in b:
        i.append(b)
print(b[0])
