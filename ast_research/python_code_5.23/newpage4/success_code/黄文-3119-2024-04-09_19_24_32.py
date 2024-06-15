# 获取输入并使用eval将其转换为列表
input_list = eval(input())

# 创建一个空列表，用于存储结果
result_list = []

# 反向遍历输入的列表
for item in reversed(input_list):
    # 如果元素不在结果列表中，将其添加到结果列表的开头
    if item not in result_list:
        result_list.insert(0, item)

# 输出结果列表
print(result_list)

