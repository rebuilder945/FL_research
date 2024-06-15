names = input().split(',')

scores = eval(input())
result = [[name, score] for name, score in zip(names, scores)]
print(result)
