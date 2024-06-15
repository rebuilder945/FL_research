scores=[]
for i in range(3):
    name,english,python,math=map(str,input().split((" ")))
    english=int(english)
    python=int(python)
    math=int(math)
    avg=(english+python+math)/3
    avg=round(avg,2)
    stu=dict(name=name,english=english,python=python,math=math,avg=avg)
    scores.append(stu)
lst1=[]
l=len(scores)
while l>0:
    jishu=scores[0]["avg"]
    for i in scores:
        if i["avg"]>jishu:
            jishu=i["avg"]
    for i in scores:
        if i["avg"]==jishu:
            lst1.append(i)
            scores.remove(i)
            l-=1
print(lst1)
        






