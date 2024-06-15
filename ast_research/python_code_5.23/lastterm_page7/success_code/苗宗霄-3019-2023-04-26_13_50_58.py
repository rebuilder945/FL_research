# 输入学生姓名和各科成绩，将其存储到字典stu中
stu = {"name":input(), "english":float(input()), "python":float(input()), "math":float(input())}

# 计算平均成绩并添加到字典中
avg_score = round((stu["english"] + stu["python"] + stu["math"]) / 3, 2)
stu["avg"] = avg_score

# 将字典中的各科成绩从高到低排序
sorted_scores = sorted(stu.items(), key=lambda x: -x[1])    # 利用items()方法得到一个由(key, value)构成的列表，按value排序

# 输出结果
print(stu["name"], end=" ")
for item in sorted_scores:
    if item[0] != "name":
        print("{:.2f}".format(item[1]), end=" ")
print("{:.2f}".format(stu["avg"]))

