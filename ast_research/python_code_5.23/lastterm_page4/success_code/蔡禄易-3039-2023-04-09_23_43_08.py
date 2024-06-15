a = list(input().split())
for i in a:
    if max(a) == i:
        a.remove(i)
    break
for c in a:
    if min(c) == i:
        a.remove(c)
    break
print(a)
