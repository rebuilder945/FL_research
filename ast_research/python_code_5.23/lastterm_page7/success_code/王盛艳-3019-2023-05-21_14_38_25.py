stu = {}
s = input()
s = s.split(" ")
#取出成绩放入列表并按从大到小排序
score = [int(s[1]),int(s[2]),int(s[3])]
score = sorted(score,reverse =True)
#依次从列表取出数据放到学生字典相应的键中
stu["name"] = s[0]
stu["english"] = int(s[1])
stu["python"] = int(s[2])
stu["math"] = int(s[3])
stu["avg"] = (stu["english"]+stu["python"]+stu["math"])/3
r = []
r.append(stu["name"])
r.append(score[0])
r.append(score[1])
r.append(score[2])
r.append(stu["avg"])
print("%s %.2f %.2f %.2f %.2f"%(r[0],r[1],r[2],r[3],r[4]))
