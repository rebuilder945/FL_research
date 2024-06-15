a=eval(input())
b=a.copy()
max=max(b)
min=min(b)
for x in b:
    if max in a:
        a.remove(max)
for x in a:
    if min in b:
        a.remove(min)
print(a)
