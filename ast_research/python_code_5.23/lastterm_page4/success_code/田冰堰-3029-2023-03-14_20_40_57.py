list1=input()
list2=eval(input())
combinelist=[]
for i in range(len(list1)):
    li=[]
    li.append(list1[i])
    li.append(list2[i])
    combinelist.append(li)
print(combinelist)
