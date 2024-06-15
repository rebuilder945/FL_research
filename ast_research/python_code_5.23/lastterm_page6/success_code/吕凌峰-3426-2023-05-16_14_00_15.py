# 分段函数求值
# 【问题描述】
# 编写一个程序，用户输入一个值x，计算分段函数f(x)的值并输出结果
# 函数f(x)请用自定义函数实现
def f(x):
    if x < 20:
        Output = 6 * x ** 2 + 1
    if x >= 20 and x < 40:
        Output = (3 * x - 60) ** 0.5
    if x >= 40:
        Output = 100 / (x + 1)
    return '%.2f' %Output
x = eval(input())
print(f(x))
