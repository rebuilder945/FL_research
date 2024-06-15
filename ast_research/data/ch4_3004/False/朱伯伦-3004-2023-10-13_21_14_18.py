list1=eval(input())
list2=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,93,97]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
    else:
        continue
print(list3)

