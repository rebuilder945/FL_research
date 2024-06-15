name = input()  # 输入飞机名称
a = float(input())  # 输入加速度
v = float(input())  # 输入起飞速度

length = round(v**2 / (2*a), 2)  # 计算最短跑道长度，保留两位小数

# 输出结果
print("The acceleration of {} is {:.2f} M / s, the take-off speed is {:.2f} M / s, and the shortest take-off runway length is {:.2f} M.".format(name, a, v, length))


