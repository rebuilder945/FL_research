word_counts = {}
while True:
    word = input()
    if word == "q":
        break
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
most_common_word = max(word_counts, key=word_counts.get)
print(most_common_word, word_counts[most_common_word])

