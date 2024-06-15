import operator
name=input().split(",")
grade=eval(input())
print(grade)
finlsit=[]
for i in list(range(len(name))):
    x=[]
    x.append(name[i])
    x.append(grade[i])
    finlsit.append(x)
finlsit.sort(key=operator.itemgetter(1))
print(finlsit)
