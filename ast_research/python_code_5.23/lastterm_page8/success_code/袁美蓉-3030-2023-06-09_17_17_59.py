name = input().split(",")
grade = input().split(",")
list = []
for i in range(len(name)):
    list.append([name[i],int(grade[i])])
list.sort(key = lambda x:x[1],reverse = False)
print(list)


