a=eval(input())
b=max(a)
c=min(a)
del a[b]
del a[c]
d=a.copy()
for x in a:
    if x==b or x==c:
        d.remove(x)
print(d)        
