lst = eval(input())
lst2 = []
for i in lst:
    if i in lst2:
        continue
    else:
        lst2.append(i)
print(lst2)

