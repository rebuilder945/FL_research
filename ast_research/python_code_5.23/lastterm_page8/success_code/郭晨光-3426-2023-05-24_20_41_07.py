# 定义自定义函数f(x)
def f(x):
    if x < -1:
        return -1 / x
    elif x >= -1 and x < 1:
        return x ** 2
    else:
        return x - 1

# 读取用户输入的x值
x = float(input())

# 调用自定义函数f(x)计算结果，并输出结果
result = f(x)
print('%.2f' % result)

