names = input().split(',')
scores_str = input()[1:-1] 
scores = list(map(int, scores_str.split(',')))
result = []
for i in range(len(names)):
    result.append([names[i], scores[i]])
print(result)
