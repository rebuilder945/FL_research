list1 = eval(input())
list1.reverse()
list2 =[]
for i in list1:
    list2.append(i)
    if i not in list2:
        list2.insert(0,i)
list2.pop()
print(list2)



