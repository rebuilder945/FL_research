# 1.输入学生成绩并存储到字典stu中
stu = {"name":"zhang"}
name, english, python, math = input().split()
stu["english"] = int(english)
stu["python"] = int(python)
stu["math"] = int(math)

# 2.计算平均成绩并添加到字典中
avg_score = round((stu["english"] + stu["python"] + stu["math"]) / 3, 2)
stu["avg"] = avg_score

# 3.由高到低排序该学生的各科成绩
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)

# 4.输出该学生的姓名，各科成绩和平均成绩
print(stu["name"], end=" ")
for score in sorted_scores:
    print("%.2f" % score, end=" ")
print("%.2f" % avg_score)

