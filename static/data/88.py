student = eval(input("请输入学生信息："))

info = tuple(student[0:1])

avg = sum(student) / len(student)
#尝试对一个类型对象进行切片操作，这是不允许的

print(info)
print("%.2f" % avg)