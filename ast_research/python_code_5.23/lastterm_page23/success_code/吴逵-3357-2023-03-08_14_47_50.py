name = input("输入飞机的名称：")
a = float(input("输入加速度a："))
v = float(input("输入起飞速度v："))
length = round(v * v / (2 * a), 2)
print("The acceleration of {} is {:.2f} M / s, the take-off speed is {:.2f} M / s, and the shortest take-off runway length is {:.2f} M.".format(name, a, v, length))

