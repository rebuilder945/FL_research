# 读取输入字符串并将其拆分为列表
input_str = input()
str_list = input_str.split()

# 计算每个字符串出现的次数
count_dict = {}
for s in str_list:
    if s in count_dict:
        count_dict[s] += 1
    else:
        count_dict[s] = 1

# 找到出现次数最多的字符串
max_count = max(count_dict.values())
max_strs = []
for s, count in count_dict.items():
    if count == max_count:
        max_strs.append(s)

# 按照升序输出结果
max_strs.sort()
for s in max_strs:
    print(s, max_count)


