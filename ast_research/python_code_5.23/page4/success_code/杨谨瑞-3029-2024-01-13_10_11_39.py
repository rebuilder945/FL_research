names=input().split(',')
scores=int(input()).split(',','[',']')
resalt=[[names[i],scores[i]]for i in range(len(names))]
print(resalt)

