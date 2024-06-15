# 从键盘输入整数列表
input_list = eval(input().strip())

# 计算平均值
average = sum(input_list) / len(input_list)

# 判断结果是否有小数部分
if average.is_integer():
    print(int(average))
else:
    print('{:.2f}'.format(average))


