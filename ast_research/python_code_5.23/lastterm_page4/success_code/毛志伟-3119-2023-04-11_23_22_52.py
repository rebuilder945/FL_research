a = eval(input())
b = []
for i in range(len(a)-1):
    if a[i] not in b:
        b.append(a[i])
print(b)
