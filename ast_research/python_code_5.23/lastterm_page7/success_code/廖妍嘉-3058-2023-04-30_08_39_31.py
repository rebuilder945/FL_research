word_count = {}
while True:
    s = input()
    if s == 'q':
        break
    if s in word_count:
        word_count[s] += 1
    else:
        word_count[s] = 1
max_count = max(word_count.values())
for word, count in word_count.items():
    if count == max_count:
        print(word, count)
        break
