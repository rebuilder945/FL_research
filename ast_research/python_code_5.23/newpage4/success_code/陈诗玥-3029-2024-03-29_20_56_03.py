names = input().split(',')
scores = input().strip('[]').split(',')
scores = [int(score) for score in scores]
name_score = [[names[i],scores[i]] for i in range(len(names))]
print(name_score)
