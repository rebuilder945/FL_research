x = 1
y = 2
n = eval(input("请输入一个整数："))
s = 0

for i in range(0, n):
    z = y / x
    y = y + x
    x = y
    s = s + z

print("%.4f" % s)  # 将格式化字符串放入print函数中进行输出