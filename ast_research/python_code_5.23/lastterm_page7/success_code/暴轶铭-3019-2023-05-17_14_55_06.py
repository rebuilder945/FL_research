stu = {"name": "", "english": 0, "python": 0, "math": 0}

# 输入学生姓名及成绩并存储到字典中
name, english, python, math = input().split()
stu["name"] = name
stu["english"] = float(english)
stu["python"] = float(python)
stu["math"] = float(math)

# 计算平均成绩并存储到字典中
average = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = average

# 将字典中每个成绩按照从高到低排序
sorted_scores = sorted(stu.items(), key=lambda item: item[1], reverse=True)

# 输出姓名，各科成绩和平均成绩，并将成绩保留两位小数
print(sorted_scores[0][1], end=' ')
for i in range(1, 4):
    print("%.2f" % sorted_scores[i][1], end=" ")
print("%.2f" % average)
