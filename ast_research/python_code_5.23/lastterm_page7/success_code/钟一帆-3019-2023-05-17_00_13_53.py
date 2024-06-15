s=input().split(' ')
stu={}
gra={}
stu["english"]=float(s[1])
stu["python"]=float(s[2])
stu["math"]=float(s[3])
gra=stu.copy()
stu["name"]=s[0]
stu["avg"]=(float(s[1])+float(s[2])+float(s[3]))/3
score=list(gra.items())
score.sort(reverse=True,key=lambda x:x[1])
print('%s %.2f %.2f %.2f %.2f'%(stu["name"],int(score[0][1]),int(score[1][1]),int(score[2][1]),stu["avg"]))


