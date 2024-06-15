name=input().split(',')
grade=eval(input())
a=[]
for x in range(len(grade)):
    b=[]
    b.append(name[x])
    b.append(grade[x])
    a.append(b)
print(a)
