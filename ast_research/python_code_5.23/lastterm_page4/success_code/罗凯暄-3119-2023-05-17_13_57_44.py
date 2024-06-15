# 输入一个列表
lst = eval(input())

# 创建一个空字典用于存储元素出现的位置
pos_dict = {}

# 遍历列表中的每个元素
for i in range(len(lst)):
    # 如果该元素已经在字典中出现过，更新其位置
    if lst[i] in pos_dict:
        pos_dict[lst[i]] = i
    # 如果该元素是第一次出现，将其加入字典
    else:
        pos_dict[lst[i]] = i

# 根据字典中记录的位置信息，将最后一个重复元素保留下来
new_lst = []
for i in range(len(lst)):
    if i == pos_dict[lst[i]]:
        new_lst.append(lst[i])

# 输出去重后的列表
print(new_lst)

