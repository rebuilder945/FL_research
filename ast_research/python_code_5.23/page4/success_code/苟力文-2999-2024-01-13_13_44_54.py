# 输入字符串
input_str = input()
# 将字符串转换为列表
input_list = input_str.split()
# 输入两个整数n和m
n, m = map(int, input().split())
# 交换列表中对应位置的元素
input_list[n], input_list[m] = input_list[m], input_list[n]
# 打印输出交换后的列表
print(input_list)

