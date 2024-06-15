lst = eval(input())
lst_copy = lst.copy()
for i in lst:
    if i == 0:
        m = lst.index(i)
        del lst_copy(m)
        lst_copy.append(m)
    else:
        pass
print(lst_copy)

