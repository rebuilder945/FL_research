name,english,python,math=input().split()
stu={}
stu["name"]=name
stu["english"]=int(english)
stu["python"]=int(python)
stu["math"]= int(math)
avg = (stu["english"]+stu["python"]+stu["math"])/3
stu["avg"]=avg
del stu["name"]
score = []
for k,v in stu.items():
    score.append([k,v])
score.sort(key=lambda x:x[1],reverse=True)
print(name,"%.2f %.2f %.2f"%(score[0][1],score[1][1],score[2][1]))

