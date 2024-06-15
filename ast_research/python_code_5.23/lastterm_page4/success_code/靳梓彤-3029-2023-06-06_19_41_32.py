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
print(lst)
lst=[[name[i],score[i]] for i in range(len(name))]
