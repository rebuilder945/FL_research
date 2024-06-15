# 读取输入的字符串列表
input_list = input().split()

# 读取两个整数n和m，表示要交换的位置
n, m = map(int, input().split())

# 检查n和m是否在列表范围内
if 0 <= n < len(input_list) and 0 <= m < len(input_list):
    # 交换列表中索引为n和m的元素
    input_list[n], input_list[m] = input_list[m], input_list[n]

# 输出交换后的列表
print(input_list)

