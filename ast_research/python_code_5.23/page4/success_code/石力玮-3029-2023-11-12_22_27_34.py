name=input()
grade=eval(input())
new=[]
listname=name.split(',')
for i in range(len(grade)):
    new.append(list(listname[i],grade[i]))
print(new)

