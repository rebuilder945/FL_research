list1=input()
list2=eval(input())
list3=[]
for x in range(len(list1)):
    list4=[]
    list4.append(list1[x])
    list4.append(list2[x])
    list3.append(list4)
print(list3)
