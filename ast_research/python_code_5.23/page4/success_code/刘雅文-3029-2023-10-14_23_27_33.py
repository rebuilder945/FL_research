name=input().split(',')
list1=list(name)
grade=eval(input())
list3=[]
for x in range(len(list1)):
    list2=[]
    list2.append(list1[x])
    list2.append(grade[x])
    list3.append(list2)
print(list3)
