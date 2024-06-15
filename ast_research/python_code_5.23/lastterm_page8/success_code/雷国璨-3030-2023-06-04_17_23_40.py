names = input().split(',')
scores = list(map(int, input().split(',')))
result = [[names[i], scores[i]] for i in range(len(names))]
result.sort(key=lambda x: x[1]) 
print(result)
