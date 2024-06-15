from collections import Counter
s = input()
lst = s.split()
cnt = Counter(lst)
max_count = max(cnt.values())
max_strings = sorted([s for s in cnt.keys() if cnt[s] == max_count])
for s in max_strings:
    print(s, max_count)


