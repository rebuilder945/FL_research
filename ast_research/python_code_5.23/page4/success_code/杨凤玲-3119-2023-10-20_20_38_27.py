a = eval(input())
b = []
for i in range (len(a)):
    if a[i:].count(a[i]) == 1:
        b.append(a[i])
print(b)

