names=input().split(',')
scores=input().split(',')
scores=list(map(int(scores)))
lsts=[]
for x in range(len(names)):
    lsts.append([names[x],scores[x]])
print(lsts)
