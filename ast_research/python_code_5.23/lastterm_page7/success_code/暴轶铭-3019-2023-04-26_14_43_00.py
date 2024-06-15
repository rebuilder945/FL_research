#1.输入学生成绩，并存储到字典stu中
stu={"name":"zhang"}
line = input().split()
stu["english"] = int(line[1])
stu["python"] = int(line[2])
stu["math"] = int(line[3])

#2.计算学生的平均成绩，同时在字典中添加关键字"avg"
avg_score = round((stu["english"] + stu["python"] + stu["math"]) / 3, 2)
stu["avg"] = avg_score

#3.将字典按照value从高到低排序
sorted_scores = sorted(stu.items(), key=lambda x: -x[1]) #降序排序

#4.输出学生的姓名、各科成绩和平均成绩
out_str = "{}".format(stu["name"])
for key, value in sorted_scores:
    if key != "name":
        out_str += " {:.2f}".format(float(value))
out_str += " {:.2f}".format(avg_score)
print(out_str)
