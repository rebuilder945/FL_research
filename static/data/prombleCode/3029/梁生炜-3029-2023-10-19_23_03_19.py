name = input().split(",")
score = eval(input())
students=[]
for i in range(len(name)):
    x = name[i]+score[i]
    a=[]
    a.append(x)
    students.append(a)
print(score,type(score))
