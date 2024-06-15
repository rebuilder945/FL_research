name=input().split(',')
grade=input().split(',')
stu=[]
for i in range(len(name)):
    stu.append((name[i],int(grade[i])))
stu.sort(key=lambda x:x[1])
lt=[]
for i in stu:
    lt.append(list(i))
print(lt)


