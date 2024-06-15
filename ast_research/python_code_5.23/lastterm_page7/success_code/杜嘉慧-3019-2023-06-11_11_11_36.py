stu={}
s=input().split()
stu["name"]=s[0]
stu["english"]=eval(s[1])
stu["python"]=eval(s[2])
stu["math"]=eval(s[3])
stu["avg"]=(stu["name"]+stu["english"]+stu["math"])/3
score=[]
score.append(stu["english"])
score.append(stu["python"])
score.append(stu["math"])
score.sort(reverse=True)
print(stu["name"],end=" ")
for i in range(len(score)):
    print("%.2f"%(score[i]),end=" ")
print("%.2f"%(stu["avg"]))
