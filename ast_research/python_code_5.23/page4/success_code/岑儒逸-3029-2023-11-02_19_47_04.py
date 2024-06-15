name=input().split(',')
score=eval(input())
final=[]
for i in range(0,len(score)):
    sim=[]
    sim.append(name[i])
    sim.append(score[i])
    final.append(sim)
print(final)
