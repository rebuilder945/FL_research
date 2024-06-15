list=input().split()
stu = {"name": list[0], "english": float(list[1]), "python": float(list[2]), "math": float(list[3])}

# 计算平均成绩并添加到字典中
avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg_score

# 从高到低排序学生的各科成绩
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)

# 输出学生姓名、各科成绩和平均成绩
print(stu["name"], end=" ")
for score in sorted_scores:
    print("{:.2f}".format(score), end=" ")
print("{:.2f}".format(avg_score))

