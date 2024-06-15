str_list = eval(input())  # 读入字符串列表

# 初始化字母计数器
counter = {}
for i in range(26):
    counter[chr(ord('a') + i)] = 0

# 遍历字符串列表，统计每个字母出现次数
for s in str_list:
    for c in s:
        counter[c] += 1

# 按字母顺序输出每个字母出现次数
for i in range(26):
    c = chr(ord('a') + i)
    if counter[c] > 0:
        print(c + ',' + str(counter[c]))

