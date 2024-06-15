stu = {"name": "", "english": 0, "python": 0, "math": 0}

# 输入学生姓名及各科成绩
info = input().split()
stu["name"] = info[0]
stu["english"] = float(info[1])
stu["python"] = float(info[2])
stu["math"] = float(info[3])

# 计算平均成绩并添加到字典中
total_score = stu["english"] + stu["python"] + stu["math"]
avg_score = total_score / 3
stu["avg"] = avg_score

# 对成绩由高到低排序
sorted_scores = sorted(stu.items(), key=lambda x: x[1], reverse=True)[1:]

# 输出结果
print(stu["name"], end=" ")
for score in sorted_scores:
    print("%.2f" % score[1], end=" ")
print("%.2f" % avg_score)
