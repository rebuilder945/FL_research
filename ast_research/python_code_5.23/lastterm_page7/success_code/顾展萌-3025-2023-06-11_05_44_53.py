s = input().split()

word_dict = {}
max_count = 0
for word in s:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    max_count = max(max_count, word_dict[word])

result_list = []
for word in sorted(word_dict):
    if word_dict[word] == max_count:
        result_list.append((word, max_count))

for elem in result_list:
    print(elem[0], elem[1])

