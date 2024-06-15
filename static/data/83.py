student = eval(input())
info = tuple([student[1], student[3]])  # 使用逗号来分隔这两个索引，而不是放在一个元组中
avg = sum(student[-1]) / len(student[-1])
print(info)
print("%.2f" % avg)