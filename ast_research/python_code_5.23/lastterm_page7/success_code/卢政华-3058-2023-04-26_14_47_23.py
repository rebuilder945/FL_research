word_dict = {}
max_word = ''
max_count = 0

while True:
    word = input()
    if word == 'q':
        break
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
    if word_dict[word] > max_count:
        max_count = word_dict[word]
        max_word = word

print(max_word, max_count)
