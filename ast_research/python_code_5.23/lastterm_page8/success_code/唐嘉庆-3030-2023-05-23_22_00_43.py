name=input().split(',')
grade=input().split(',')
grade.sort()
jack=[]
for i in range(len(name)):
    a,b=name[i],eval(grade[i])
    jack.append([a,b])
print(jack)
