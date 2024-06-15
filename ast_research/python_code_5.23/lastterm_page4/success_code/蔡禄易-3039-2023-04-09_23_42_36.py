a = list(input().split())
for i in a:
    if max(a) == i:
        a.remove(i)
    break
for i in a:
    if min(a) == i:
        a.remove(i)
    break
print(a)
