# 从键盘输入列表
input_list = eval(input().strip())

# 创建一个空字典用于存储元素及其最后一次出现的位置
last_occurrence = {}
for i, num in enumerate(input_list):
    last_occurrence[num] = i

# 保留每个元素的最后一次出现位置
output_list = [input_list[i] for i in sorted(last_occurrence.values())]

# 输出结果
print(output_list)

