stu = {"name": "", "english": 0, "python": 0, "math": 0}

# 读取输入并存储到字典中
name, eng, py, math = input().split()
stu["name"] = name
stu["english"] = int(eng)
stu["python"] = int(py)
stu["math"] = int(math)

# 计算平均分并存储到字典中
avg = (stu["english"] + stu["python"] + stu["math"]) / 3
stu["avg"] = avg

# 对字典中的成绩进行排序
sorted_scores = sorted(stu.items(), key=lambda x: x[1], reverse=True)

# 输出排序后的各科成绩和平均分
print(stu["name"], end=" ")
for i in range(1, 4):
    print("%.2f" % sorted_scores[i][1], end=" ")
print("%.2f" % avg)
