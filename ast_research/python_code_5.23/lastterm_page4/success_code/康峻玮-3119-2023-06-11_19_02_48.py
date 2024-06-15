input_list = eval(input())  # 读入列表

exist_set = set()     # 记录出现过的元素
output_list = []      # 记录输出的列表
for i in range(len(input_list)-1, -1, -1):  # 倒序遍历列表中的元素
    if input_list[i] not in exist_set:      # 如果该元素还没有出现过
        output_list.insert(0, input_list[i])   # 将其插入到输出列表的最前面（保留最后一个）
        exist_set.add(input_list[i])            # 将该元素添加到出现集合中

print(output_list)
