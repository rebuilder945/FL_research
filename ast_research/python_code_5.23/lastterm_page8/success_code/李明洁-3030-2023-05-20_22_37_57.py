names = input().split(',')
scores = list(map(int,input().split(',')))
s = []
for i in names:
    s.append(i)
for i in scores:
    s.append(i)
print(s,reverse = True)
