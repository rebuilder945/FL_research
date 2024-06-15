a=eval(input())
max=max(a)
min=min(a)
for x in a:
    if max in a:
        a.remove(max)
for y in a:
    if min in a:
        a.remove(min)
print(a)
