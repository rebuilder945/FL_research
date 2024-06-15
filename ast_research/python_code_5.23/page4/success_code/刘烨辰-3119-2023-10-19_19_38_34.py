list1 = eval(input())
list2 = list1.copy()
for x in list1:
    for y in list2:
        if list1.count(x) > 1:
            for i in range(0,list2.count(y)-1):
                list2.remove(y)
print(list2)
