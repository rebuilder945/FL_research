student = eval(input())
info = student[1], student[2]
avg = sum(student[5]) / len(student[5])#sum(student[5]) 返回一个浮点数，其不可作为迭代对象
print(info)
print("%.2f" % avg)