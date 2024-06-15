s = input("飞机名称为:")
a = float(input("飞机加速度是(m/s^2):"))
v = float(input("起飞速度(m/s):"))
length = (v**2) / (2*a)
print("跑道长度为:%.2f"%length)

