a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for x in a:
    if b in d:
        a.remove(b)
    if c in d:
        a.remove(c)
print(a)
