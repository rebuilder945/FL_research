a = str(input())
b = eval(input())
list1 = list(a)
list2 = list(b)
list3 = []
for i in range(len(list1)):
    list4 = [list1[i],list2[i]]
    list3.append(list4)
print(list3)
