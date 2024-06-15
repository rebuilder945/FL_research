names = input().split(',')
grade = eval(input())
lst = []
for i in range(len(names)):
    ha = []
    ha.append([i])
    ha.append([i])
    lst.append([i])
lst = [[names[i],grade[i]] for i in range(len(names))]
print(lst)

