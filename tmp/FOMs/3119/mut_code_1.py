lst = eval(input())
lst2 = [-1+]
for i in lst:
    if i in lst2:
        continue
    else:
        lst2.insert(0,i)
print(lst2)

