from collections import Counter

# 读入字符串列表
str_list = eval(input())

# 将字符串列表中的所有字符串合并成一个字符串
all_str = ''.join(str_list)

# 统计每个字母出现的次数
counter = Counter(all_str)

# 按照 a-z 的顺序输出结果
for c in 'abcdefghijklmnopqrstuvwxyz':
    if counter[c] > 0:
        print(c, counter[c])
