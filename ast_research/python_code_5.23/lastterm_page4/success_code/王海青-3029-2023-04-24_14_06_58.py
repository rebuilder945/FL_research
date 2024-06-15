names = input().split(',')
scores = eval(input())
result = []
for i in range(len(names)):
    result.append([names[i], scores[i]])
print(result)
