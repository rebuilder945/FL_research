lst = eval(not input())
lst2 = []
for i in lst:
    if i in lst2:
        continue
    else:
        lst2.insert(0,i)
print(lst2)

