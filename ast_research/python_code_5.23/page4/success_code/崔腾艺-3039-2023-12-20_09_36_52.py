a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for x in d:
    if x==b:
        a.remove(b)
    if x==c:
        a.remove(c)
print(a)
