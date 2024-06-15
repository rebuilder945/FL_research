name=list(input().split(","))
grade=eval(input())
lb=[]
for i in range(len(name)):
    result=[]
    result.append(name[i])
    result.append(grade[i])
    lb.append(result)
print(lb)
