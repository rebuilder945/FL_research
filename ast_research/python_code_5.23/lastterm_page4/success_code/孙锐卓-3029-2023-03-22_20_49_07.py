names = input().split(",")
scores_str = input()
scores = eval(scores_str)
result = []
for i in range(len(names)):
    result.append([names[i], scores[i]])
print(result)
