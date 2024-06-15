x = input()
list1 = [int(list1) for list1 in x]
list2 = []
for i in list1:
    i = (i+5)%10
    list2.append(i)
list2[0],list2[-1]= list2[-1],list2[0]
list2[1],list2[-2]= list2[-2],list2[1]
print(*list2,sep = "")
