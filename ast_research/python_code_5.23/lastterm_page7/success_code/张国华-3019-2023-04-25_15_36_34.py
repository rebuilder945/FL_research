# 从键盘读入学生姓名及三门课程的成绩，并将其存储到一个字典中
stu = {"name": input(), "english": float(input()), "python": float(input()), "math": float(input())}
# 根据字典中的成绩计算平均成绩，并将其添加到字典中
avg = sum(stu.values() - stu["name"]) / 3
stu["avg"] = avg
# 对字典中的成绩进行排序
stu1=stu.copy()
del stu1["name"]
sorted_scores = sorted(stu1.items(), key=lambda x: x[1], reverse=True)
# 输出学生姓名、各科成绩和平均成绩
print(stu["name"], end=' ')
for score in sorted_scores[1:]:
    print('{:.2f}'.format(score[1]), end=' ')
print('{:.2f}'.format(avg))
