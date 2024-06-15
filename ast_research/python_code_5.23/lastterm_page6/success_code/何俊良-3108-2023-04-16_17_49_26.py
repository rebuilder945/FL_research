string_list = eval(input().strip())  # 读取字符串列表
count_dict = {}  # 用于记录每个字母的出现次数

for string in string_list:
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    if char in count_dict:
        print("%s,%s" % (char, count_dict[char]))

