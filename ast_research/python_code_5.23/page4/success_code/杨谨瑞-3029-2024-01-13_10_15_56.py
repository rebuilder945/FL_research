names=input().split(',')
scores = input()[1:-1].split(',') 
resalt=[[names[i],int(scores[i])]for i in range(len(names))]
print(resalt)

