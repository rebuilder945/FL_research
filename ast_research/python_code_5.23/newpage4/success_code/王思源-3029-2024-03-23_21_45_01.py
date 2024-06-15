name = list(input().split(','))
grade = eval(input())
results = []
for i in range(len(name)):
    result = []
    result.append(name[i])
    result.append(grade[i])
    results.append(result)

print(results)
