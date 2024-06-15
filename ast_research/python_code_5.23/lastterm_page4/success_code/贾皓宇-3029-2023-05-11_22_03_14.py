names=list(input())
scores=eval(input())
c=[x for x in range(len(names)-3)]
mix=[[names[i],scores[i]] for i in c]
print(mix)


