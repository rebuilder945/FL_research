names = input().split(",")
grade = eval(input())
a = []
for x in range(len(names)):
    a.append([names[x],grade[x]])
print(a)
