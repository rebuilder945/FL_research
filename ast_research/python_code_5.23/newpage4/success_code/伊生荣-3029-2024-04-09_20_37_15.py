names = input().split(',')
scores = input()[1:-1].split(',')
result = [[name,int(score)] for name,score in zip (names,scores)]
print(result)
