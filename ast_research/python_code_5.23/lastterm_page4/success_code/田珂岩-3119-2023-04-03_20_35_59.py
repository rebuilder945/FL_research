list1 = eval(input())
list2 = list1.copy()
for i in list1:
    if (i not in list2):
        list2.append(i)
print(list2)        
