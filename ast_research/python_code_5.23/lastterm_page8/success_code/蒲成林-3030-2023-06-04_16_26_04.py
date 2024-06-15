names = input().split(',')
scores = list(map(int, input().split(',')))

result = list(zip(names, scores))
result.sort(key=lambda x: x[1])

print(result)
