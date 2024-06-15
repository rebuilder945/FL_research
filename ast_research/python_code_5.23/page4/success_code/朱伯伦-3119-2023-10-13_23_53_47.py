list1 =eval(input())
list2 = []
for each in range(len(list1)-1, -1, -1):
    if list1[each] not in list2:
        list2.append(list1[each])
list2.reverse()
print(list2)
