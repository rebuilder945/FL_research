s=[]
grade=[]
name=input().split(',')
grade2=input().split(',')
for i in grade2:
    i=int(i)
    grade.append(i)
for i in range(len(name)):
    [x,y]=[name[i],grade[i]]
    s.append([x,y])
    s.sort(key=lambda x:x[1])
print(s)
