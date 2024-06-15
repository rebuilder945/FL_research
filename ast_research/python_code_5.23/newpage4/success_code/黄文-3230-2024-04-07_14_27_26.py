def largest_number(digits):
    # 将字符串的数字排序，并拼接成一个新的字符串
    # 注意，这里使用了额外的字符'0'来确保在比较时不区分数字和字母'0'
    sorted_s = ''.join(sorted(digits, reverse=True))
    # 过滤掉排序后字符串中的'0'，因为它们不会影响最终结果
    largest_num = ''.join(filter(lambda x: x != '0', sorted_s))
    return largest_num if largest_num else '0'

# 读取输入，假设输入是一个由逗号分隔的数字字符串
input_str = input("请输入一个正整数列表（每个数字只有一位），用逗号分隔：")

# 将输入的字符串分割成一个列表
digits = list(map(int, input_str.split(',')))

# 计算并输出结果
print(largest_number(digits))



