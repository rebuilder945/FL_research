stu={}
msg = input()
msg = msg.split(" ")
#取出成绩放入列表进行从大到小的排序
score=[int(msg[1]),int(msg[2]),int(msg[3])]
score = sorted(score,reverse=True)
stu["name"]=msg[0]
stu["english"]=int(msg[1])
stu["python"]=int(msg[2])
stu["math"]=int(msg[3])
stu["avg"]= (stu["english"]+stu["python"]+stu["math"])/3
#把结果按题目要求放入列表
result = []
result.append(stu["name"])
result.append(score[0])
result.append(score[1])
result.append(score[2])
result.append(stu["avg"])
print("%s %.2f %.2f %.2f %.2f" % (result[0] ,result[1] , result[2]  ,result[3] , result[4] ))
