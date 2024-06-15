from collections import defaultdict

# 使用 defaultdict 创建一个默认值为0的字典
word_dict = defaultdict(int)

while True:
    s = input()
    if s == 'q':
        break
    word_dict[s] += 1

# 找出出现次数最多的字符串
max_word = ''
max_count = 0
for word, count in word_dict.items():
    if count > max_count:
        max_word = word
        max_count = count

print(max_word, max_count)
