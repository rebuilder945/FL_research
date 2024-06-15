a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for x in d:
    if x==b:
        a.pop(b)
    if x==c:
        a.pop(c)
print(a)
