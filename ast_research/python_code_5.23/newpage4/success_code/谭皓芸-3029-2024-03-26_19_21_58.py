names = input().split(',')
scores_str = input()[1:-1].split(',')
scores = [int(score) for score in scores_str]
result = [[name, score] for name, score in zip(names, scores)]
print(result)
