stu = {} # 字典初始化

# 输入学生信息
name = input("请输入学生姓名：")
english = float(input("请输入英语成绩："))
python = float(input("请输入Python成绩："))
math = float(input("请输入数学成绩："))

# 将学生信息存储到字典中
stu["name"] = name
stu["english"] = english
stu["python"] = python
stu["math"] = math

# 计算平均成绩并添加到字典中
avg = (english + python + math) / 3.0
stu["avg"] = avg

# 对成绩从高到低排序
sorted_scores = sorted([english, python, math], reverse=True)

# 输出学生信息
print("姓名：", stu["name"])
print("英语成绩：%.2f" % stu["english"])
print("Python成绩：%.2f" % stu["python"])
print("数学成绩：%.2f" % stu["math"])
print("平均成绩：%.2f" % stu["avg"])

# 输出排序后的各科成绩
print("各科成绩从高到低排序：", sorted_scores)


