names = list(input().split(','))
grades = list(eval(input()))
x1 = []
for i in range(len(names)):
    x = []
    x.append(names[i])
    x.append(grades[i])
    x1.append(x)
grades.sort()
x2 = []
for i in range(len(grades)):
    for j in range(len(x1)):
        if x1[j][1] == grades[i]:
            x2.append(x1[j])
print(x2)
