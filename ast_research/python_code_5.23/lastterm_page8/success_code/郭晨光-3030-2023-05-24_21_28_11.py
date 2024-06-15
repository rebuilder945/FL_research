names = input().split(',')
scores = input().split(',')
pairs = list(zip(names, scores))
sorted_pairs = sorted(pairs, key=lambda x: int(x[1]))
nested_list = [[pair[0], int(pair[1])] for pair in sorted_pairs]
print(nested_list)

