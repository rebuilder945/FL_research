stu = {}
scores = input().split()
scores = [float(score) for score in scores]

# 计算平均成绩
avg_score = sum(scores) / len(scores)
avg_score = round(avg_score, 2)

# 将学生姓名、各科成绩和平均成绩存储到字典中
stu["name"] = "Zhang"
stu["english"] = scores[0]
stu["python"] = scores[1]
stu["math"] = scores[2]
stu["avg"] = avg_score

# 输出学生信息
print(" ".join([str(value) for value in stu.values()]))
