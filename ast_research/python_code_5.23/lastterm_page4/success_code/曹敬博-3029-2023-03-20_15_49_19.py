names = eval(input())
scores = eval(input())
result = []
for i in range(len(names)):
    result.append([names[i],int(scores[i])])
print(result)
