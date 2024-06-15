l=eval(input())
a=max(l)
b=min(l)
l1=l.copy()
for x in l1:
    if x==a:
        l.remove(x)
for y in l1:
    if y==b:
        l.remove(y)
print(l)
