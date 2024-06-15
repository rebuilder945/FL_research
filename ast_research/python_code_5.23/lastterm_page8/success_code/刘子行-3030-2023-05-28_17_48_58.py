name=input().split()
score=input().split()
score1=map(int,score)
mix=list(zip(name,score1))
mix1=[]
for x in mix:
    mix1.append(list(x))
mix2=sorted(key=lambda x:x[1])
print(mix2)

