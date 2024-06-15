name=input()
name=list(name)

grade=eval(input())
List=[]
m=[]
for i in range(len(name)) :
    m.append(name[i])
    m.append(grade[i])
    List.append(m)
print(List)
