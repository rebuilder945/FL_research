student = eval(input())
info = student[2:5]
info = [float(x) for x in info]  # 将列表中的元素转换为浮点数
avg = sum(info) / len(info)
print(info)
print("%.2f"%avg)

