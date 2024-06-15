names=input().split(',')
scores=eval(input())
c=[x for x in range(len(names))]
mix=[[names[i],scores[i]] for i in c]
print(mix)



