names=input().split(' , ')
scores=input()[1:-1].split(',')
result=list(zip(names,map(int,scores)))
result=[[name,score] for name,score in result]
print(result)
