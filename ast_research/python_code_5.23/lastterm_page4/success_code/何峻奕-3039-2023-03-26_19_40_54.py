l=eval(input())
a=max(l)
b=min(l)
l1=l.copy()
for x in l1:
    if x==a:
        l.remove(x)
    print(l)
    if x==b:
        l.remove(x)
    print(l)
