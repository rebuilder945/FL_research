def largest_number(s):
    # 从输入字符串中提取所有数字字符
    digits = [int(c) for c in s if c.isdigit()]
    # 将数字字符转换为字符串并逆序排序
    digits_str = ''.join(sorted(map(str, digits), reverse=True))
    # 将排序后的字符串转换回整数
    largest_num = int(digits_str)
    return largest_num

# 读取输入
input_str = input()
# 计算并输出最大的整数
print(largest_number(input_str))

