# 存储学生信息
stu = {"name": "Zhang", "english": 80, "python": 90, "math": 100}

# 输入学生姓名以及三门课的分数
name, english, python, math  = input().strip().split()

# 更新学生信息
stu["name"] = name
stu["english"] = int(english)
stu["python"] = int(python)
stu["math"] = int(math)

# 计算学生平均分
avg_score = round((stu["english"] + stu["python"] + stu["math"]) / 3, 2)

# 更新学生信息
stu["avg"] = avg_score

# 由高到低排序该学生的各科成绩
sorted_scores = sorted(stu.values(), reverse=True)[1:]

# 输出学生信息
print(stu["name"], end=" ")
for score in sorted_scores:
    print("{:.2f}".format(score), end=" ")
print("{:.2f}".format(avg_score))
