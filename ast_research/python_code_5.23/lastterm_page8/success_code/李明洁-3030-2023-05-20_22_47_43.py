names = input().split(',')
scores = list(map(int,input().split(',')))
s = [].split(',')
for i in names:
    s.append(i)
for i in scores:
    s.append(i)
s = sorted(scores,reverse=False)
print(s)
