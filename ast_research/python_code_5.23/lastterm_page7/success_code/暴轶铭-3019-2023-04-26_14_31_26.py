# 1. 输入学生的信息
stu = {"name": "", "english": 0, "python": 0, "math": 0}

stu["name"] = input("请输入学生姓名：")
stu["english"] = float(input("请输入英语成绩："))
stu["python"] = float(input("请输入python成绩："))
stu["math"] = float(input("请输入数学成绩："))

# 2. 计算平均成绩并添加到字典中
average_score = round((stu["english"] + stu["python"] + stu["math"]) / 3, 2)
stu["avg"] = average_score

# 3. 对各科成绩进行排序
sorted_scores = sorted([(k, v) for k, v in stu.items() if k != "name"],
                       key=lambda x: x[1], reverse=true)

# 4. 输出学生的信息
print(f"姓名：{stu['name']}")
for item in sorted_scores:
    print(f"{item[0]}：{item[1]:.2f}")
print(f"平均成绩：{average_score:.2f}")
