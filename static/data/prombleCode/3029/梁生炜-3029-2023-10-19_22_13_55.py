name = input().split(",")
score = input().split(",")
s = [int(score[i])for i in range(len(score))]
students=[]
for i in range(len(name)):
    x = name[i],score[i]
    a=[]
    a.append(x)
    students.append(a)
print(students)
