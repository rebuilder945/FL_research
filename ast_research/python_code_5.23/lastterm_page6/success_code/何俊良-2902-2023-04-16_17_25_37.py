def get_sum(n):
    """  计算数列前n项和
    """
    # 初始化数列中的前两项
    a, b = 2, 1
    sum_num = 0
    for i in range(n):
        sum_num += a / b
        a, b = a + b, a
    return sum_num


# 读取输入，调用函数，并输出结果
n = int(input().strip())
sum_num = get_sum(n)
print("{:.4f}".format(sum_num))

