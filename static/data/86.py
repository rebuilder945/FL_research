# 获取用户输入的学生信息
student_info = input("请输入学生信息：")
student = eval(student_info)
avg = student

print("学生信息：", student)
print("平均值：%.2f" % avg)