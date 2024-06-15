num_list = eval(input())  # 输入的列表
num_str = ''.join(map(str, num_list))   # 将列表中的数字转换为字符串并拼接起来
num_set = set(num_str)   # 将字符串中的字符去重得到集合
num_set_sorted = sorted(num_set, reverse=True)   # 对集合中的字符进行排序，降序排列
result_str = ''.join(num_set_sorted)   # 将排序后的字符拼接起来得到最大整数的字符串表示
result_int = int(result_str)   # 将字符串转换为整数
print(result_int)   # 输出最大整数

