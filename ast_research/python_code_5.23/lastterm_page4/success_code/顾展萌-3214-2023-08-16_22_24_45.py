lst = eval(input())
lst1 = []
lst2 = []
for i in lst:
    if i == 0:
        lst1.insert(0,i)
    else:
        lst2.insert(-1,i)
lst3 = lst2 + lst1

print(lst3)




