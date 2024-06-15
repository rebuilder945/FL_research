# 读取输入的整数列表
input_list = list(map(int, input().split(',')))

# 读取输入的n和m
n, m = map(int, input().split(','))

# 检查n是否在列表下标范围内
if 1 <= abs(n) <= len(input_list):
    # 选择第n个元素，重复m次，放到列表的尾端
    selected_element = input_list[abs(n) - 1]
    repeated_elements = [selected_element] * m
    updated_list = input_list + repeated_elements

    # 输出列表
    print(updated_list)
else:
    # 输出错误信息
    print("error")

