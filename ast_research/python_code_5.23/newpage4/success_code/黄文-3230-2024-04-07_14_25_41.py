def largest_number(digits):
    # 将列表转换为字符串，并连接起来形成一个长字符串
    # 这样做是为了能够对数字进行排序，而不考虑它们的位置
    s = ''.join(map(str, digits))
    # 对字符串进行排序，生成一个排序后的字符串
    # 注意，这里使用了额外的字符'0'来确保在比较时不区分数字和字母'0'
    sorted_s = ''.join(sorted(s, reverse=True))
    # 过滤掉排序后字符串中的'0'，因为它们不会影响最终结果
    largest_num = ''.join(filter(lambda x: x != '0', sorted_s))
    return largest_num

# 读取输入
digits = list(map(int, input().split()))

# 计算并输出结果
print(largest_number(digits))



