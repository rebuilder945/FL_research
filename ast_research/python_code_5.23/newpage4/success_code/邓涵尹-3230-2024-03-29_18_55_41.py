def max_integer(num_list):
    num_count = [0] * 10  # 初始化一个包含10个元素的列表，用于记录每个数字的出现次数
    for num in num_list:
        num_count[num] += 1  # 统计每个数字出现的次数

    max_num = ''  # 初始化最大整数的字符串表示形式
    for i in range(9, -1, -1):  # 从9到0逆序遍历数字
        max_num += str(i) * num_count[i]  # 将数字按照出现次数拼接到最大整数字符串中

    return int(max_num)  # 将字符串表示的最大整数转换为整数并返回

# 测试输入列表
input_list = eval(input()) # 或者 [2, 3, 1, 2, 0]

# 计算最大整数
result = max_integer(input_list)

# 输出最大整数
print(result)

