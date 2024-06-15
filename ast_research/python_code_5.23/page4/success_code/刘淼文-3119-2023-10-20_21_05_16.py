lst = eval(input())
lst2 = []
for i in lst:
    if lst.count(i) > 1:
        continue
    else:
        lst2.append(i)
print(lst2)

