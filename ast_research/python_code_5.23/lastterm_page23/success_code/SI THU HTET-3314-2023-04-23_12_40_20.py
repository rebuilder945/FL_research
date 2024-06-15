square_feet = float(input())  # 输入土地面积（平方英尺）
acres = round(square_feet / 43560, 3)  # 计算土地面积对应的英亩数，保留三位小数

# 输出结果
print("The land area is {:.3f}".format(acres))


