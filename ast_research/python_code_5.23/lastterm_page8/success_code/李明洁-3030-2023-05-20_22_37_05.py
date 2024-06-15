names = input().split(',')
scores = list(map(int,input().split(',')))
s = []
for i in range(len(names)):
    for j in range(len(scores)):
        s.append(names[i],scores[j])
s.sort(reverse=True)
print(s)
