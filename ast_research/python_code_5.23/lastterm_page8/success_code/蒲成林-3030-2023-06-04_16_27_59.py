names = input().split(',')
scores = list(map(int, input().split(',')))

result = [[name, score] for name, score in zip(names, scores)]
result.sort(key=lambda x: x[1])

print(result)

