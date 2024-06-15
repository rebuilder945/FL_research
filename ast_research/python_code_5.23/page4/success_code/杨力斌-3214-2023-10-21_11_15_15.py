lst = eval(input())
lst_copy = lst.copy()
for i in lst:
    if i == 0:
        m = lst.index(i)
        lst_copy.remove(i)
        lst_copy.append(0)
    else:
        pass
print(lst_copy)

