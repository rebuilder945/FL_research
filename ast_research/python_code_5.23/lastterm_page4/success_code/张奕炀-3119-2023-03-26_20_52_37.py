list1 = eval(input())
list1 = list1[::-1]
list2 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
list2 = list2[::-1]
print(list2)
