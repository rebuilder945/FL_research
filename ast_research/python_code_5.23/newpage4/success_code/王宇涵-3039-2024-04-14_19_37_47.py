lst = eval(input())
lst1 = lst.copy()
a = max(lst)
b = min(lst)
for x in lst:
    if x==a or x==b:
        lst1.remove(x)
print(lst1)
