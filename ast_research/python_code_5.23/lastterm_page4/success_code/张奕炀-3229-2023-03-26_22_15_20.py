list1 = eval(input())
list2 = []
list3 = list1.copy()
list4 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
for i in range(len(list2)):
    list3.remove(list2[i])
for i in range(len(list3)):
    if list3[i] not in list4:
        list4.append(list3[i])
for x in range(len(list4)):
    for i in range(len(list1)-1,-1,-1):
        if list1[i] == list4[x]:
            list1.remove(list4[x])
list1.sort(reverse = False)
for i in range(len(list1)):
    list1[i] = str(list1[i])
string = ','.join(list1)
if string == True:
    print(string)
else:
    print(False)
