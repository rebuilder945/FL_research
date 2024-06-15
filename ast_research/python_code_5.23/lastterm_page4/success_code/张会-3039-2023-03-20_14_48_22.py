lst = eval(input())
a = min(lst)
b = max(lst)
c = lst.copy()
for i in lst:
    if i==a or i==b:
        c.remove(i)
print(c)
