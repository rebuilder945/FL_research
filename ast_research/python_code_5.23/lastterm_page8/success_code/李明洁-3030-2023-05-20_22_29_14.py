names = input().split()
scores = list(map(int,input().split()))
s = []
for i in range(len(names)):
    s.append(names[i],scores[i])
s.sort(reverse=True)
print(s)
