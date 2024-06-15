lst = eval(input())
lst1 = []
lst2 = []
for i in lst:
    if i != 0:
        lst1.append(i)
    else:
        lst2.append(i)
lst1.extend(lst2)
print(lst1)


