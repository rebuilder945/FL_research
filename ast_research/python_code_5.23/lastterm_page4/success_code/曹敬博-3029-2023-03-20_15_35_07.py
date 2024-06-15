names = input().split(',')
scores = input().split(',')
result = []
for i in range(len(names)):
    result.append((names[i],int(scores[i])))
    print(result)
