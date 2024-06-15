words = {}
while True:
    word = input("请输入一个字符串（输入 q 结束）：")
    if word == 'q':
        break
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

max_word = ''
max_count = 0
for word, count in words.items():
    if count > max_count:
        max_word = word
        max_count = count

print("出现次数最多的字符串为：{}，出现次数为：{}".format(max_word, max_count))



