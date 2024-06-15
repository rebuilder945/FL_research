# 输入学生的名字和各科成绩
stu = {"name": "zhang", "english": 80, "python": 90, "math": 100}

# 计算平均成绩，并在字典中添加关键字"avg"
avg = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg

# 排序学生各科成绩
sorted_stu = sorted(stu.items(), key=lambda x: x[1], reverse=True)

# 输出学生的姓名、各科成绩和平均成绩
print(sorted_stu[0][1], "%.2f" % sorted_stu[1][1], "%.2f" % sorted_stu[2][1], "%.2f" % sorted_stu[3][1], "%.2f" % avg)
