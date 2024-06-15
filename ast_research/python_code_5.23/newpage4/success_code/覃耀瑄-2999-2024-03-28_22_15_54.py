# 输入列表
input_list = input().split()

# 输入要交换的位置
n, m = map(int, input().split())

# 交换元素值
input_list[n], input_list[m] = input_list[m], input_list[n]

# 输出交换后的列表
print(input_list)

