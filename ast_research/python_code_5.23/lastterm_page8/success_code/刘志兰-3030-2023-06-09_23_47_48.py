name=input().split(',')
sname=[name]
score=eval(input())
sscore=[score]
students=list(zip(sname,score))
students_sorted=sorted(students, key=lambda x:x[1])
print(students_sorted)

