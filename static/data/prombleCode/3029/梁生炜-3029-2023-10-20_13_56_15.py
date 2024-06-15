name = input().split(",")
score = eval(input())
students=[]
for i in range(len(name)):
    x=[name[i],score[i]]
    students.append(x)
print(students)
