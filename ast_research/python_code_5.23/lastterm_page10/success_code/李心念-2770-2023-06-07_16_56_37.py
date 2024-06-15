a = sorted(list(input()))
b = sorted(list(input()))
n = True
for x in range(len(a)):
    if a[x] == b[x]:
        break
    else:
        n = False
print(n)
