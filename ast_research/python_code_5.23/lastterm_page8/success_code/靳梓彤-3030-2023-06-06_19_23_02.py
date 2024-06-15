name=input().split(",")
score=input().split(",")
for i in range(len(name)):
    a=name[i]
    b=score[i]
    stu=[a,"%i"%b]
    lst=[]
    lst.append(stu)
lst.sort(key=lambda score:score[1])
print(lst)
