# 读取输入的正整数列表
input_list = eval(input())

# 将列表中的数字按照字符串表示形式排序
sorted_str_list = sorted(map(str, input_list), reverse=True)

# 将排序后的字符串连接起来形成一个整数
max_integer = int(''.join(sorted_str_list))

# 输出最大整数
print(max_integer)

