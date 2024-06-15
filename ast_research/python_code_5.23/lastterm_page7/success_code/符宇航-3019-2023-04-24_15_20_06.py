stu=input().split(' ')
name=stu.pop(0)
stu=list(map(int,stu))
stu.sort(reverse=True)
x=sum(stu)/len(stu)
stu.append(x)
print(name,end=' ')
for i in stu:
    print('%.2f'%i,end=' ')

