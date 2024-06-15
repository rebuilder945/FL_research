a=eval(input())
b=a.copy()
max=max(b)
min=min(b)
for x in a:
    if max in a:
        a.remove(max)
for y in a:
    if min in a:
        a.remove(min)
print(a)
