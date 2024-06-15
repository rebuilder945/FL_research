list1 = eval(input())
list2 = list1.copy()
for a in list1:
    count = list2.count(a)
    if count > 1:
        while count > 1:
            list2.remove(a)
            count -= 1
print(list2)
