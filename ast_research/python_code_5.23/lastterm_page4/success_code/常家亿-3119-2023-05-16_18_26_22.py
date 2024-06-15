lst = eval(input())
lst1 = lst.copy()
for x in lst:
    if lst.count(x)>1:
        lst1.remove(x)
    else:
        pass
print(lst1)

