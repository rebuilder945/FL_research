name=input().split(',')
grade=eval(input())
sbname=list(name)
a=()
b=[]
for i in range(len(sbname)):
    a=(sbname[i],grade[i])
    b.append(list(a))
print(b)

