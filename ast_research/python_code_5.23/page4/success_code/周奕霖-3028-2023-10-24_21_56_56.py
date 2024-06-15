names = input().split(',')
scores = eval(input())
a = list(zip(names,scores))
students = []
for x,y in a:
    student = [x,y]
    students.append(student)
print(students)

