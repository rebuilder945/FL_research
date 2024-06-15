a = list(input.split())
for i in a:
    if max(a) == i:
        b = a.index(i)
        del a[b]
    break
for i in a:
    if min(a) == i:
        c = a.index(i)
        del a[c]
    break
print(a)
