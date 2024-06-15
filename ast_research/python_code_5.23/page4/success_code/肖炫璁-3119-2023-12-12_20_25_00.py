# 读取输入的列表
input_list = eval(input())

# 创建一个字典来跟踪每个元素的最后一个索引
last_index = {}
for i, elem in enumerate(input_list):
    last_index[elem] = i

# 根据字典创建新的列表，保留每个元素的最后一个出现位置
output_list = [elem for elem, idx in last_index.items()]

# 输出删除重复值后的列表
print(output_list)

