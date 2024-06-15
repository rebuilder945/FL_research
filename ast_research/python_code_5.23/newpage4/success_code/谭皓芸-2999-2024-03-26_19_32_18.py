# 读取输入的字符串列表
input_str = input().split()

# 读取需要交换的位置
n, m = map(int, input().split())

# 交换列表中对应位置的元素
input_str[n], input_str[m] = input_str[m], input_str[n]

# 输出交换后的列表
print(input_str)

