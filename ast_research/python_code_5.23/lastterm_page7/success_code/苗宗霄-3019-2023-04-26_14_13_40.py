# 读取输入
name, eng, python, math = input().split()

# 存储成绩到字典中
stu = {"name": name, "english": float(eng), "python": float(python), "math": float(math)}

# 计算平均成绩并添加到字典中
avg_score = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg_score

# 由高到低排序各科成绩
sorted_scores = sorted([stu["english"], stu["python"], stu["math"]], reverse=True)

# 输出结果
print(stu["name"], "{:.2f}".format(sorted_scores[0]), "{:.2f}".format(sorted_scores[1]), "{:.2f}".format(sorted_scores[2]), "{:.2f}".format(avg_score))

