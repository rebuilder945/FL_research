stu={"name":"Zhang"}

# 读取学生姓名及成绩并存储到字典中
s = input()
name, english, python, math = s.split()
stu["english"] = int(english)
stu["python"] = int(python)
stu["math"] = int(math)

# 计算平均成绩并添加到字典中
avg = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg

# 按照成绩从高到低排序
scores = [stu["english"], stu["python"], stu["math"]]
scores.sort(reverse=True)

# 输出结果
print(stu["name"], "%.2f" % scores[0], "%.2f" % scores[1], "%.2f" % scores[2], "%.2f" % avg)

