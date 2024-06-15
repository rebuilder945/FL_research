name = input().split(',')
grade = eval(input())
lst=[]
for i in range(len(name)):
    item = []
    item.append(name[i])
    item.append(grade[i])
    lst.append(item)
print(lst)
