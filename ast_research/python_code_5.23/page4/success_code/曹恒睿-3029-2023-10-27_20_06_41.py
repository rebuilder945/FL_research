name = input().split(",")
grade = eval(input())
zongrenshu = len(grade)
for x in range(0,zongrenshu):
    n=[]
    n1 = name.pop(0)
    n2 = grade.pop(0)
    n.append(n1)
    n.append(n2)
    print(n)




