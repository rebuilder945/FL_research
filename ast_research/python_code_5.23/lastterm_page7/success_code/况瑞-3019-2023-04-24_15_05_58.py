score=[]
for i in range(5):
    stu={}
    stu["name"]="Zhang"+str(i)
    stu["english"]=80+i
    stu["python"]=90+i
    stu["math"]=100+i
    score.append(stu)
for i in range(len(score)):
    avg=(score[i]["english"]+score[i]["python"]+score[i]["math"])/3
    score[i]["avg"]=avg
print(score)
print(sorted(score,key=lambda x:x["avg"],reverse=True))

