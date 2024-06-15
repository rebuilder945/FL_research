# 1. 存储学生姓名及成绩
stu = {"name":"zhang"}
english = input()
python = input()
math = input()

stu["english"] = int(english)
stu["python"] = int(python)
stu["math"] = int(math)

# 2. 计算平均成绩并添加到字典中
avg = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg

# 3. 由高到低排序各科成绩
score_list = [stu["english"], stu["python"], stu["math"]]
score_list.sort(reverse=True)

# 4. 输出学生信息
print(stu["name"], '{:.2f}'.format(score_list[0]), '{:.2f}'.format(score_list[1]), '{:.2f}'.format(score_list[2]), '{:.2f}'.format(avg))
