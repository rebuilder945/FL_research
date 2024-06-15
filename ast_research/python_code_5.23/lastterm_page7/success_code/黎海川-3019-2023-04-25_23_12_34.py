stu={"name":"","english":"","python":"","math":""}
stu["name"] = input("请输入学生姓名：")
stu["english"] = float(input("请输入英语成绩："))
stu["python"] = float(input("请输入Python成绩："))
stu["math"] = float(input("请输入数学成绩："))
avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg_score
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)
print("姓名：", stu["name"])
print("英语成绩：{:.2f}".format(stu["english"]))
print("Python成绩：{:.2f}".format(stu["python"]))
print("数学成绩：{:.2f}".format(stu["math"]))
print("平均成绩：{:.2f}".format(stu["avg"]))


