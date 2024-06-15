names = input().split(",")
scores = list(map(int, input().split(",")))
name_score = [[name, score] for name, score in zip(names, scores)]
name_score = sorted(name_score, key=lambda x: x[1])
print(name_score)
