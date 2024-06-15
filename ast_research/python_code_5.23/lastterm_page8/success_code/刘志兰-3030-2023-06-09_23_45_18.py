sName=[input().split(",")]
score=[input()]
students=list(zip(sName,score))
students_sorted=sorted(students, key=lambda x:x[1])
print(students_sorted)

