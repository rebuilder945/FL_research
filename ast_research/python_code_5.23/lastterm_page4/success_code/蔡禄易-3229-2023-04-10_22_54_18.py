list1 = eval(input())
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.insert(0,i)
    else:
        print(False)
        break
list2.sort()
print(list2)

