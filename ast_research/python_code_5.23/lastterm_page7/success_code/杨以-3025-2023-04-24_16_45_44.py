from collections import Counter


input_str = input()


counter = Counter(input_str.split())


max_count = max(counter.values())
max_strings = sorted([s for s in counter if counter[s] == max_count])


for s in max_strings:
    print(s, max_count)
