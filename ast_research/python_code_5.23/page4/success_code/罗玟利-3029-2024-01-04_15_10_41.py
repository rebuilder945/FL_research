names = input().split(',')
scores = [int(x) for x in input().strip('[]').split(',')]
result = [[names[i], scores[i]] for i in range(len(names))]
print(result)

