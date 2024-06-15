name=input().split(",")
score=input().split(",")
for i in range(3):
    a=name[i]
    b=score[i]
    stu=[a,b]
    lst=[]
    lst.append(stu)
lst.sort(key=lambda score:score[1])
print(lst)
