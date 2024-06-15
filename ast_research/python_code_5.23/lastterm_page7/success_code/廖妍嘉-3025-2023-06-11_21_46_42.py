from collections import Counter
s = input().split()
counter = Counter(s)
max_count = max(counter.values())
for word, count in sorted(counter.items()):
    if count == max_count:
        print(word, count)

