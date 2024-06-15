# 从键盘输入列表
input_list = input().strip()
num_list = eval(input_list)

# 计算平均值
average = sum(num_list) / len(num_list)

# 判断小数部分是否为0
if average % 1 == 0:
    # 如果小数部分为0，输出整数部分
    print(int(average))
else:
    # 如果小数部分不为0，输出结果保留两位小数
    print("{:.2f}".format(average))

