e=eval(input())
b=max(e)
c=min(e)
d=e.copy()
for x in e:
    if x==c or x==b:
        d.remove(x)
print(d)
