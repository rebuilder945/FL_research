names = input().split(',')
scores = list(map(int, input().split(',')))
nested_list = list(zip(names, scores))
sorted_list = sorted(nested_list, key=lambda x: x[1])
print(sorted_list)

