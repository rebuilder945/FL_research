names = input().split(',')
scores = eval(input())
c = []
for i in range(0,len(names)):
    temp = [',']
    temp.append(names[i])
    temp.append(scores[i])
    c.append(temp)
c.sort(key = lambda temp:temp[1],reverse=False)
print(c)
