name, english, python, math = input().split()

# 将成绩转化为浮点数类型
english = float(english)
python = float(python)
math = float(math)

# 创建字典并存储数据
stu = {"name": name, "English": english, "python": python, "math": math}

# 计算平均成绩并添加到字典中
avg_score = round(sum(stu.values() - stu["name"]) / 3, 2)
stu["avg"] = avg_score

# 对字典中的成绩进行排序
score_list = sorted(stu.values() - stu["name"] - stu["avg"], reverse=True)

# 输出结果
print(stu["name"], end="")
for score in score_list:
    print(" {:.2f}".format(score), end="")
print(" {:.2f}".format(avg_score))
