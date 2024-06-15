names = input().split(',')
scores = [int(score) for score in input().split(',')]
result = [[name,score] for name,score in zip(names,scores)]
print(result)
