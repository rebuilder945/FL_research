a=eval(input())
b=max(a)
c=min(a)
for x in a:
    if b in a:
        a.remove(b)
    if c in a:
        a.remove(c)
print(a)
