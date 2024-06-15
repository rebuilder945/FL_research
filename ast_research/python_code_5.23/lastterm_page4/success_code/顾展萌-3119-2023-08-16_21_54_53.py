lst = eval(input())
lst1 = []
lst.reverse()
for i in lst:
    if i not in lst1:
        lst1.append(i)
    else:
        pass
lst1.reverse()
print(lst1)
