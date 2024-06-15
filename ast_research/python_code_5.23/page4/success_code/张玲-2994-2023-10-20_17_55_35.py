# 从键盘输入整数列表
input_list = input().strip().split(',')
input_list = [int(num) for num in input_list]

# 从键盘输入n和m
n, m = input().strip().split(',')
n = int(n)
m = int(m)

# 判断n是否在列表下标范围内
if abs(n) < len(input_list):
    # 选择第n个元素并重复m次
    selected_element = input_list[n]
    output_list = input_list + [selected_element] * m
    print(output_list)
else:
    print("error")

