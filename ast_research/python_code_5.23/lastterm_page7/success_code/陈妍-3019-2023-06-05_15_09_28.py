info=input().split()
stu={}
stu['name'],stu['english'],stu['python'],stu['math']=info[0],eval(info[1]),eval(info[2]),eval(info[3])
score=[]
score.append(stu['english'])
score.append(stu['python'])
score.append(stu['math'])
score.sort(reverse=True)
stu['avg']="%.2f"%((stu['english']+stu['python']+stu['math'])/3)
print(stu['name'],end=" ")
for i in range(len(score)):
    print("%.2f"% score[i],end=" ")
print(stu['avg'])
