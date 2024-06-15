a=eval(input())
b=max(a)
c=min(a)
for b in a:
    a.remove(b)
    for c in a:
        a.remove(c)
print(a)
