# 读取用户输入的字符串，使用 split() 函数将字符串以空格为分隔符转换为列表
input_str = input("请输入一串字符串：")
str_list = input_str.split()

# 初始化一个字典，记录各个字符串出现的次数
str_dict = {}
for str in str_list:
    if str in str_dict:
        str_dict[str] += 1
    else:
        str_dict[str] = 1

# 找到出现次数最多的字符串及其出现次数
max_count = max(str_dict.values())
max_str_list = []
for k, v in str_dict.items():
    if v == max_count:
        max_str_list.append(k)

# 将出现次数最多的字符串按照升序排序并输出
max_str_list.sort()
for max_str in max_str_list:
    print(max_str, max_count)
