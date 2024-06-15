# 读取输入的整数列表
input_list = eval(input())

# 移动数值为0的元素到列表尾部，保持其他元素的相对顺序不变
non_zero_elements = [num for num in input_list if num != 0]
zero_elements = [num for num in input_list if num == 0]

adjusted_list = non_zero_elements + zero_elements

# 输出调整后的列表
print(adjusted_list)

