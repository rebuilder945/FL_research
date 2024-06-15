name=input().split('.')
grade=eval(input())
xname=list(name)
a=()
b=[]
for i in range(len(grade)):
    a=(xname[i],grade[i])
    b.append(list(a))
print(b)
