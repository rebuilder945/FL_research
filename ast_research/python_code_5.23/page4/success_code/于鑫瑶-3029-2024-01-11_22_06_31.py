name=input().split(",")
ls3=list(name)
grade=eval(input())
ls1=[]
ls4=()
for i in range(len(name)):
    ls4=[name[i],grade[i]]
    ls1.append(ls4)
print(ls1)

