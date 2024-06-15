# 1. 输入学生姓名和各科成绩
name = input()
english_score = float(input())
python_score = float(input())
math_score = float(input())

# 将学生信息存储到字典中
stu = {"name": name, "english": english_score, "python": python_score, "math": math_score}

# 2. 计算平均成绩并添加到字典中
avg_score = (english_score + python_score + math_score) / 3
stu["avg"] = avg_score

# 3. 按照成绩由高到低排序
sorted_scores = sorted([(k, v) for k, v in stu.items() if k != "name"], key=lambda x: x[1], reverse=True)

# 4. 输出学生信息
print(stu["name"])
for subject, score in sorted_scores:
    print("{:.2f}".format(subject.capitalize(), score))
print("{:.2f}".format(stu["avg"]))

