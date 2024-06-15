names = input().split(',')
scores = eval(input())
c = []
for i in range(0,len(names)):
    temp = []
    temp.append(names[i])
    temp.append(scores[i])
    c.append(temp)
c=sorted(scores,reverse=False)
print(c)
