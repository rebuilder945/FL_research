s = input()  # 读取输入的字符串
words = s.split()  # 将字符串按照空格分割成一个列表

# 统计每个字符串出现的次数
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

# 找出出现次数最多的字符串及其出现次数
max_count = max(count.values())
max_words = [k for k, v in count.items() if v == max_count]
max_words.sort()  # 按照键的升序排序

# 输出结果
for word in max_words:
    print(word, max_count)

