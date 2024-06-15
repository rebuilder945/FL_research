# 读入多个字符串并转为列表
str_list = input().split()

# 读入n和m的值
n, m = map(int, input().split())

# 交换n和m位置上的元素
str_list[n], str_list[m] = str_list[m], str_list[n]

# 输出交换后的列表
print(str_list)


