names = input().split(',')
scores = list(map(int, input().split(',')))
data = [[name, score] for name, score in zip(names, scores)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
