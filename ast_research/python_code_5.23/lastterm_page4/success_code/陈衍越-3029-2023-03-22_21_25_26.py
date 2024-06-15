names=input().split(',')
grade=eval(input())
lst=[]
for i in range(len(names)):
    item=[]
    item.append(names[i])
    item.append(grade[i])
    lst.append(item)
print(lst)

