lst = eval(input())
lst1 = []
lst2 = lst.reverse()
for i in lst2:
    if lst2.count(i) == 1:
        lst1.append()
    else:
        if i not in lst1:
            lst1.append(i)
lst3 = lst1.reverse()
print(lst3)
