names = list(str,input().split(','))
scores = list(map(int,input().split(',')))
s =[',']
for i in range (names):
    s.append(names[i])
for i in range (scores):
    s.append(scores[i])
s = sorted(scores,reverse=False)
print(s)
