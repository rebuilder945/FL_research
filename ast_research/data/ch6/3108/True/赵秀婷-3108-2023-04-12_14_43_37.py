lst = eval(input())

# 初始化字典，每个字母出现次数为 0
count_dict = {}
for i in range(97, 123):
    count_dict[chr(i)] = 0

# 统计每个字母出现的次数
for s in lst:
    for c in s:
        count_dict[c] += 1

# 按 a-z 的顺序输出字母出现次数
for i in range(97, 123):
    if count_dict[chr(i)] > 0:
        print("{},{}".format(chr(i), count_dict[chr(i)]))

