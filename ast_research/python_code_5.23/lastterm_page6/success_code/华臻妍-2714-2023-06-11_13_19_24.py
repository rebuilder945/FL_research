score = float(input("请输入百分制成绩："))

# 将百分制成绩转换为五分制成绩
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

# 输出五分制成绩和对应的等级
print("五分制成绩为：%s，对应等级为：%s" % (grade, score))
