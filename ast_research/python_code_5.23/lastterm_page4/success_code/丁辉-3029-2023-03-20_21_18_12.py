name=input().split(',')
score=input()
a=[]
for x in range(len(score)+1):
    a.append([name[x],score[x]])
print(a)

