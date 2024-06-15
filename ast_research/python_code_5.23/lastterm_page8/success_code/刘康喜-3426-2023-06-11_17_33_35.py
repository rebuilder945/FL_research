def f(x):

    if  x < 20:
        return (6*x ** 2 + 1)
    elif x < 40:
        return (3*x-60)**0.5
    else:
        return 100/(x+1)

x = float(input())  # 读入 x 值
result = f(x)  # 计算 f(x) 值
print("%.2f" % result)  # 输出结果，保留小数点后两位
