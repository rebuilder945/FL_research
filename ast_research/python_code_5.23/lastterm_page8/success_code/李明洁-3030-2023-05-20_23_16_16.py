names = list(str,input().split(','))
scores = list(map(int,input().split(',')))
s =[',']
for i in len(names):
    s.append(names[i])
for i in len(scores):
    s.append(scores[i])
s = sorted(scores,reverse=False)
print(s)
