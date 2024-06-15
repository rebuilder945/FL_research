name = input().split(",")
score = input().split(",")
students=[]
for i in range(len(name)):
    x = name[i]+score[i]
    a=[]
    a.append(x)
    students.append(a)
print(students)
