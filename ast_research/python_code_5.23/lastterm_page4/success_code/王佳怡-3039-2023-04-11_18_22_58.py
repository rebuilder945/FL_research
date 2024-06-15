l=list(eval(input()))
a=max(l)
b=min(l)
l1=l.copy()
for i in l1:
    if i==a or i==b:
        l.remove(i)
print(l)
