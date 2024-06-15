# 1. 输入学生姓名及三门成绩并存储到字典stu中
stu={"name":"zhang"}
english, python, math = map(int, input().split())
stu["english"] = english
stu["python"] = python
stu["math"] = math

# 2. 计算该同学的平均成绩并添加到字典stu中
avg_score = round(sum(stu.values()[1:])/3, 2)
stu["avg"] = avg_score

# 3. 对字典stu的value进行排序（从高到低）
sorted_scores = sorted(stu.values()[1:], reverse=true)

# 4. 输出学生姓名、各科成绩和平均分（保留两位小数）
print(f'{stu["name"]} {sorted_scores[0]:.2f} {sorted_scores[1]:.2f} {sorted_scores[2]:.2f} {avg_score:.2f}')

