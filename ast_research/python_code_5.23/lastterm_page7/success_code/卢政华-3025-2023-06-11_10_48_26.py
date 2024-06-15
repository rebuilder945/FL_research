s = input()  # 读入字符串
words = s.split()  # 将字符串按照空格分割为单词列表
word_count = {}  # 用于保存每个单词出现的次数

# 统计每个单词出现的次数
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# 找出出现次数最多的单词及其出现次数
max_count = 0
max_words = []
for word, count in word_count.items():
    if count > max_count:
        max_count = count
        max_words = [word]
    elif count == max_count:
        max_words.append(word)

# 按照字典序排序输出结果
for word in sorted(max_words):
    print(word, max_count)
