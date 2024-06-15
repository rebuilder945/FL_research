name=input().split(',')
score=eval(input())
a=[]
for x in range(len(score)):
    a.append([name[x],score[x]])
print(a)

