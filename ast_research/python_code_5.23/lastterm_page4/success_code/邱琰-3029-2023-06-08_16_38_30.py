name=input().split(',')
grade=eval(input())
ls=[]
for i in range(len(grade)):
    ls.append([name[i],grade[i]])
print(ls)
