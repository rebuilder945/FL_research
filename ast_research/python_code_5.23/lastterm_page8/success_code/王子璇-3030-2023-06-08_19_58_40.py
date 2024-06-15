names=input().split(',')
scores=eval(input()).split(',')
lsts=[]
for x in range(len(names)):
    lsts.append([names[x],scores[x]])
print(lsts)
