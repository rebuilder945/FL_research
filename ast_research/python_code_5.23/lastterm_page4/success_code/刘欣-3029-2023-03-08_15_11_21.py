names = input().split(',')
scores = list(map(int, input().split(',')))
result = [[name, scores[index]] for index, name in enumerate(names)]
result.sort(key=lambda item: item[1])
print(result)
