name = input().split(",")
grade = eval(input())
a = []
for i in range(0,len(name)):
    a.append([name[i],grade[i]])
print(a)
