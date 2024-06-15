lst = eval(input())
a = max(lst)
b = min(lst)
lst1 = lst.copy()
for x in [a,b]:
    if x in lst:
        lst1.remove(x)
    else:
        pass
print(lst1)
