str_list = eval(input())  # 读入字符串列表
count_dict = {}  # 初始化空字典
for string in str_list:  # 遍历字符串列表
    for char in string:  # 遍历字符串中的每个字符
        if char in count_dict:  # 如果字典中已有该字符键
            count_dict[char] += 1  # 出现次数+1
        else:
            count_dict[char] = 1  # 否则将该字符键加入字典，出现次数为1
for key, value in sorted(count_dict.items()):  # 遍历字典中的每一项，按键排序
    print(key + ',' + str(value))  # 输出键和值，用逗号分隔
