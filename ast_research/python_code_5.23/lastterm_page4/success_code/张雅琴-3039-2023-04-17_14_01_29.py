lst=eval(input())
a=max(lst)
b=min(lst)
c=lst.copy()
for x in lst:
    if x==a or x==b:
        c.remove(x)
print(c)
