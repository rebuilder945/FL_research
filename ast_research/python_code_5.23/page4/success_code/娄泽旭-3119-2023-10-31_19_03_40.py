a = eval(input())
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
