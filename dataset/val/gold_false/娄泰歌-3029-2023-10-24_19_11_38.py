names = input().split(',')
scores = input().split(',')
result = [[name,score] for name,score in zip(names,scores)]
print(result)
