name=input().split(",")
score=input()[1:-1]
scores = list(map(int, score.split(',')))
z=[]
for i in range (len(name)):
    z.append([name[i],scores[i]])
print(z)
