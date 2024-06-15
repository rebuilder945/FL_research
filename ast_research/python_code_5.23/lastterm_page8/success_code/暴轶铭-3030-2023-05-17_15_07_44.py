namelist = input().split(",")
scorelist = input().split(",")
for i in range(len(scorelist)):
    scorelist[i] = int(scorelist[i])
students = []
for i in range(len(namelist)):
    student = [namelist[i], scorelist[i]]
    students.append(student)
students.sort(key=lambda x: x[1])
print(students)
