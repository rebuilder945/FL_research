# 输入学生的姓名及各科成绩并存储到字典stu中
stu = {"name": "zhang", "english": 80, "python": 90, "math": 100}

# 计算平均成绩并在字典中添加关键字"avg"
avg = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg

# 由高到低排序该学生的各科成绩
sorted_stu = sorted(stu.items(), key=lambda x: x[1], reverse=True)
scores = [str(score) for (_, score) in sorted_stu if type(score) == int]
sorted_scores = " ".join(scores)

# 输出姓名、各科成绩和平均成绩
print(f"{stu['name']} {sorted_scores} {avg:.2f}")
