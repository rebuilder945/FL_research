stu = {"name": "Zhang", "english": 80, "python": 90, "math": 100}
# 输入成绩信息
stu["name"] = input("请输入学生姓名：")
stu["english"] = float(input("请输入英语成绩："))
stu["python"] = float(input("请输入Python成绩:"))
stu["math"] = float(input("请输入数学成绩："))
# 计算平均成绩并添加到字典中
avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = round(avg_score, 2)
# 按照成绩由高到低排序
sorted_scores = sorted(stu.items(), key=lambda x: x[1], reverse=True)
# 输出结果
print("姓名：", stu["name"])
for k, v in sorted_scores[1:]:
    print(k.capitalize(), ":", format(v, ".2f"))
