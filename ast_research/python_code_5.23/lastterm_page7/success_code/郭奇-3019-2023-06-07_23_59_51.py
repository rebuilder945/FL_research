stu = {}

# 输入学生的成绩
name, english, python, math = input().split()
stu["name"]=name
stu["english"] = int(english)
stu["python"] = int(python)
stu["math"] = int(math)

# 计算平均成绩并添加到字典中
avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3.0
stu["avg"] = round(avg_score, 2)

# 由高到低排序各科成绩
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)

# 输出学生的姓名、各科成绩和平均成绩
print(stu["name"], end=" ")
for score in sorted_scores:
    print("{:.2f}".format(score), end=" ")
print("{:.2f}".format(stu["avg"]))
