# 判断正方形
# 【问题描述】
# 输入一个方形的长度和宽度，编写程序判断该方形是否为正方形（长和宽都应大于0）
def sqare(x, y):
    if x > 0 and y > 0:
        if x == y:
            return "It's a square"
        elif x != y:
            return "It's a rectangle"
    else:
        return 'illegal data'
a = eval(input())
b = eval(input())
print(sqare(a, b))
