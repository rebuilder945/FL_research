info=input().split()
stu={}
stu['name']=info[0]
stu['english']=eval(info[1])
stu['python']=eval(info[2])
stu['math']=eval(info[3])
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
score=[]
score.append(stu['english'])
score.append(stu['python'])
score.append(stu['math'])
score.sort(reverse=True)
print(stu['name'],end=" ")
for i in range(len(score)):
    print("%.2f"%(score[i]),end=" ")
print("%.2f"%stu['avg'])





