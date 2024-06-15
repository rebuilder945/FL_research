input_list = eval(input())
count_dict = {}

# 遍历列表中的每个字符串
for string in input_list:
    # 遍历字符串中的每个字母
    for char in string:
        # 如果字母已经在字典中，则将其计数加1
        if char in count_dict:
            count_dict[char] += 1
        # 如果字母不在字典中，则将其添加到字典中，并将计数初始化为1
        else:
            count_dict[char] = 1

# 按照a-z的顺序输出每个字母出现的次数
for char in sorted(count_dict.keys()):
    print(char + ',' + str(count_dict[char]))

