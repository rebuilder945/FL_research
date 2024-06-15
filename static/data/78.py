student = eval(input())
info = student[1], student[2]
avg = sum(student[5]) / len(student[5])  # student[5] 是一个数字列表，计算其平均值
print(info)
print("%.2f" % avg)