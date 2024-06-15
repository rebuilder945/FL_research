lst = eval(input())
lst1 = lst.copy()
for x in lst1:
    a = lst.count(x)
    if a >=2:
        for i in range(a-1):
            lst.remove(x)
print(lst)
