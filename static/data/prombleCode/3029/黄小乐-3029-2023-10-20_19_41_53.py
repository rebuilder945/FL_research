name = input().split(",")
grade = eval(input())
list = []
for i in range(len(name)):
    ls = []
    ls.append(name[i])
    ls.append(grade[i])
    list.append(ls)
print(list)

