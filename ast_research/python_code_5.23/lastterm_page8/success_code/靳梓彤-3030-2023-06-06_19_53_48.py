name=input().split(",")
score=eval(input())
lst=[]
for i in range(len(name)):
    a=name[i]
    b=score[i]
    stu=[]
    stu.append(a)
    stu.append(b)
    lst.append(stu)
lst.sort(key=lambda lst:lst[1])
print(lst)

