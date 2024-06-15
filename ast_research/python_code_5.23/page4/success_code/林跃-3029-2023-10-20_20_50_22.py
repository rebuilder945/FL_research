name=list(input().split(","))
grade=eval(input())
for i in range(len(name)):
    list2=[]
    list2.append(name[i])
    list2.append(grade[i])
print([list2])
