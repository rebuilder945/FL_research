# 输入字符串列表
str_list = input().split()

# 输入要交换的元素下标
n, m = map(int, input().split())

# 交换元素值
str_list[n], str_list[m] = str_list[m], str_list[n]

# 打印输出交换后的列表
print(str_list)
