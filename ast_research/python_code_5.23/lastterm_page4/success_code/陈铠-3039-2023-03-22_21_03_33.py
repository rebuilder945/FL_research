a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for i in d:
    if i == a or i == b:
        d.remove(i)
print(d)
