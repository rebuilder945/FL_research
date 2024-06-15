student = eval(input())
info = tuple([student[1], student[2]])  # 创建元组时应该使用逗号分隔元素，而不是将元素作为参数传递给 tuple() 函数
avg = sum(student[5]) / len(student[5])
print(info)
print("%.2f" % avg)