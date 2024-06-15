names = input().split(',')
scores = list(map(int,input().split(',')))
s = []
for i in range(len(names)):
    for i in range(len(scores)):
        s.append(names[i],scores[i])
s.sort(reverse=True)
print(s)
