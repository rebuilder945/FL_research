
# 读入学生姓名和各科成绩
line = input().split()
name, eng, py, math = line[0], float(line[1]), float(line[2]), float(line[3])

# 创建字典结构
stu = {"name": name, "english": eng, "python": py, "math": math}

# 计算平均成绩并添加到字典中
avg = (eng + py + math) / 3
stu["avg"] = avg

# 将学科成绩从高到低排序
sorted_scores = sorted(stu.values(), reverse=True)[1:]

# 输出结果
print(stu["name"], "{:.2f}".format(sorted_scores[0]), "{:.2f}".format(sorted_scores[1]),
      "{:.2f}".format(sorted_scores[2]), "{:.2f}".format(stu["avg"]))

