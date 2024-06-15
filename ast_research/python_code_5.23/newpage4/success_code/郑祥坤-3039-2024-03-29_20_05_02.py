a=eval(input())
b=max(a)
c=min(a)
d=[x for x in a]
while b in d:
    d.remove(b)
while c in d:
    d.remove(c)
print(d)
