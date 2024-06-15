a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for i in a:
    if i == a or i == b:
        d.remove(i)
print(d)
