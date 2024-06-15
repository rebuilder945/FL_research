names = input().split(',')
scores = input().strip('[]').split(',')
result = [[name, int(score)] for name, score in zip(names, scores)]
print(result)
