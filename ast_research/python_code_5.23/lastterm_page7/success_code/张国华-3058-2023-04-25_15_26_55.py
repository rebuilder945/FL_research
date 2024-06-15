# 使用一个字典来记录每个字符串的出现次数
string_count = {}
# 从键盘读取未指定个数的字符串，一行一个，以字符串"q"为输入结束标志（"q"不列入统计范围），对每个字符串进行计数
while True:
    s = input()
    if s == 'q':
        break
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
# 输出出现次数最多的字符串及其出现次数
print('{} {}'.format(max_string, max_count))

