from collections import defaultdict

word_dict = defaultdict(int)

s = input()
for word in s.split():
    word_dict[word] += 1

max_count = max(word_dict.values())
max_words = sorted([word for word, count in word_dict.items() if count == max_count])

for word in max_words:
    print(word, max_count)
