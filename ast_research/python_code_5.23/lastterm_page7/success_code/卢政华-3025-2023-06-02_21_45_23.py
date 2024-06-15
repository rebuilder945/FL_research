words = input().split()
word_dict = {}
max_count = 0

for word in words:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
    if word_dict[word] > max_count:
        max_count = word_dict[word]

max_words = sorted([word for word in word_dict if word_dict[word] == max_count])

for word in max_words:
    print(word, max_count)
