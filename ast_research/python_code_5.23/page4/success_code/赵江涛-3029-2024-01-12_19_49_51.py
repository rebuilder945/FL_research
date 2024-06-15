name = list(input().split(","))
grade = eval(input())
m = []
for x in range(len(name)):
    n = []
    n.append(name[x])
    n.append(grade[x])
    m.append(n)
print(m)
