word_dict = {}
while True:
    word = input()
    if word == 'q':
        break
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

max_word = ''
max_count = 0
for k, v in word_dict.items():
    if v > max_count:
        max_word = k
        max_count = v

print(max_word, max_count)
