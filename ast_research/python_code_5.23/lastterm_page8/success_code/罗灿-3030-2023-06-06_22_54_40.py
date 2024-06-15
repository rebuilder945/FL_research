names = input().split(',')
scores = input().split(',')
students = []
for i in range(len(names)):
    students.append([names[i], int(scores[i])])
students.sort(key=lambda x: x[1])
print(students)

