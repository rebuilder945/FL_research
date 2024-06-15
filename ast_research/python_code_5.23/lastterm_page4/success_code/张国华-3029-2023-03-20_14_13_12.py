names = input().split(',')
scores = eval(input())
result = [[names[i], scores[i]] for i in range(len(names))]
print(result)

