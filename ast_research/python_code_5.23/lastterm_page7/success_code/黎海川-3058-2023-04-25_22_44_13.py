word_dict = {}
while True:
    word = input()
    if word == "q":
        break
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
max_word =""
max_count = 0
for word, count in word_dict.items():
    if count > max_count:
        max_word = word
        max_count = count
print('%d'%max_word)
print('%d'%max_count)


