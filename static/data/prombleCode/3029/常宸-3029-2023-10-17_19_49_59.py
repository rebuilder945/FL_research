name = input().split(',')
grade = eval(input())
lst = []
for i in range(len(name)):
    item = []
    item.append(name[i])
    item.append(grade[i])
    lst = [[name[i],grade[i]] for i in range(len(name))]
    
