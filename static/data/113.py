h = float(input("请输入一个数值（作为基础值）："))
N = int(input("请输入一个整数（作为指数值）："))

s = h * (1 - 0.5**N) / 0.5
#将输入的字符串 h 转换为数值类型（例如整数或浮点数），以便进行数学运算，
#可以使用 int() 或 float() 函数来实现。

print(s)