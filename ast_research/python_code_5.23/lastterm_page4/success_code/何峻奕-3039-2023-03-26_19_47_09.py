l=eval(input())
a=max(l)
b=min(l)
l1=l.copy()
for x,y in l1:
    if x==a:
        l.remove(x)
    if x==b:
        l.remove(y)
print(l)
