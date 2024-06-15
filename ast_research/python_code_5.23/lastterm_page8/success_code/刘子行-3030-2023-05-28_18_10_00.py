name=input().split(',')
score=input().split(',')
score1=map(int,score)
mix=list(zip(name,score1))
mix1=[[name,score1] for name,score1 in mix]
mix1.sort(key=lambda x:x[1])
print(mix1)

