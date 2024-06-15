list1=list(input().split(","))
list2=list(map(eval,input().split(",")))
list3=[]
for i in range(len(list1)):
    list3.append([])
    list3[i].append(list1[i])
    list3[i].append(list2[i])
list3.sort(key=lambda x:x[1])
print(list3)
