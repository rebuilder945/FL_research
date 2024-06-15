# 使用一个字典来记录每个字符串的出现次数
string_count = {}
# 从键盘读取未指定个数的字符串，一行一个，以空格隔开，对每个字符串进行计数
for s in input().split():
    if s in string_count:
        string_count[s] += 1
    else:
        string_count[s] = 1
# 遍历字典，找出出现次数最多的字符串，并记录其出现次数
max_count = 0
max_string = ''
for string, count in string_count.items():
    if count > max_count:
        max_count = count
        max_string = string
# 遍历字典，找出所有出现次数等于最大次数的字符串，按照字符串升序输出所有符合条件的字符串及其出现次数
for string, count in sorted(string_count.items()):
    if count == max_count:
        print('{} {}'.format(string, count))
