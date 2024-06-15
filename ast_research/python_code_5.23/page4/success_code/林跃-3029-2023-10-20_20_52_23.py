name=list(input().split(","))
grade=eval(input())
list1=[]
for i in range(len(name)):
    list2=[]
    list2.append(name[i])
    list2.append(grade[i])
    list1.append(list2)
print(list1)
