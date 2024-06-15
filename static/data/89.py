student = eval(input())
# 学生信息列表需要为实数。

info = tuple(student[1:3])

avg = student[-1]

print(info)
print("%.2f" % avg)