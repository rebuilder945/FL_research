stu={"name":"","english":"","python":"","math":""}
stu["name"] = input()
stu["english"] = float(input())
stu["python"] = float(input())
stu["math"] = float(input())
avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg_score
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)
print("姓名：", stu["name"])
print("英语成绩：{:.2f}".format(stu["english"]))
print("Python成绩：{:.2f}".format(stu["python"]))
print("数学成绩：{:.2f}".format(stu["math"]))
print("平均成绩：{:.2f}".format(stu["avg"]))


