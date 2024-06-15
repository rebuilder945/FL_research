# 获取输入并使用eval将其转换为列表
input_list = eval(input())

# 找出列表中的最大值和最小值
max_value = max(input_list)
min_value = min(input_list)

# 创建一个新列表，包含原列表中除了最大元素和最小元素之外的所有元素
result_list = [x for x in input_list if x != max_value and x != min_value]

# 输出新列表
print(result_list)

