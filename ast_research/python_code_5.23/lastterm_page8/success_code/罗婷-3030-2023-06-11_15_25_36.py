names = input().split(',')
scores = input().split(',')
scores = [int(score) for score in scores]
result = [[name, score] for name, score in zip(names, scores)]
result.sort(key=lambda x: x[1])
print(result)
