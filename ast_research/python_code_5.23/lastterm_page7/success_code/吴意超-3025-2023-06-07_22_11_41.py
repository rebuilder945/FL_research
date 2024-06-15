from collections import Counter

s = input()
words = s.split()

counter = Counter(words)
max_count = max(counter.values())
most_common = sorted(word for word, count in counter.items() if count == max_count)

for word in most_common:
    print(word, max_count)
