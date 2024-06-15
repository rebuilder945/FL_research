list1 = eval(input())
list2 = []
for i in range(len(list1)):
    if list1[i] != 0:
        list2.append(list1[i])
for i in range(len(list1)):
    if list1[i] == 0:
        list2.append(list1[i])
print(list2)
