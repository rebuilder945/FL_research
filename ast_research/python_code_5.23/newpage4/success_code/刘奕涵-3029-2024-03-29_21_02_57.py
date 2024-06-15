name=input().split(',')
grade=eval(input())
list=[]
for i in range(len(name)):
    item=[]
    item.append(name[i])
    item.append(grade[i])
    list.append(item)
print(list)
